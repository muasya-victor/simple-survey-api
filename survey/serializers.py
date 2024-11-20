from rest_framework import serializers, request
from .models import Question, Response, Certificate,Choice


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question.text', read_only=True)
    selected_option_texts = serializers.SerializerMethodField()

    class Meta:
        model = Response
        fields = ['id', 'question', 'question_text', 'response_text', 'selected_options', 'selected_option_texts']

    def validate(self, data):
        question = data.get('question')
        response_text = data.get('response_text')
        selected_options = data.get('selected_options', [])

        # Ensure no existing response for the same question by the same user
        if Response.objects.filter(question=question).exists():
            raise serializers.ValidationError("You have already submitted a response for this question and cannot modify it.")

        # Ensure 'selected_options' is a list of IDs if passed as a list of dicts
        if isinstance(selected_options, list) and selected_options and isinstance(selected_options[0], dict):
            data['selected_options'] = [option.get('id') for option in selected_options]

        # Validate response based on question type
        if question.type in ['short_text', 'long_text', 'email']:
            if not response_text:
                raise serializers.ValidationError("Response text is required for this question type")
        elif question.type == 'choice':
            if not selected_options:
                raise serializers.ValidationError("Selected options are required for this question type")
            if not question.multiple and len(selected_options) > 1:
                raise serializers.ValidationError("Multiple options not allowed for this question")

        return data

    def get_selected_option_texts(self, obj):
        # Get the list of selected option texts based on the selected option IDs
        selected_option_texts = [option.option_text for option in obj.selected_options.all()]
        return selected_option_texts

    def to_representation(self, instance):
        # Get the original serialized data
        data = super().to_representation(instance)

        # Modify the representation to return both the question text and id
        question = instance.question
        data['question'] = {
            'id': question.id,
            'text': question.text
        }

        # Ensure selected_options return both id and option_text
        data['selected_options'] = [
            {'id': option.id, 'option_text': option.option_text} for option in instance.selected_options.all()
        ]

        return data


class BulkResponseSerializer(serializers.Serializer):
    responses = ResponseSerializer(many=True)

    def create(self, validated_data):
        responses_data = validated_data.get('responses', [])
        responses = []

        for response_data in responses_data:
            question = response_data.get('question')
            response_text = response_data.get('response_text')
            selected_options = response_data.get('selected_options', [])

            # Ensure selected options are IDs only
            if question.type == 'choice':
                response = Response.objects.create(
                    question=question,
                    response_text=response_text if question.type in ['short_text', 'long_text', 'email'] else None
                )
                # Assuming selected_options contains a list of IDs
                response.selected_options.set(selected_options)  # This will set the selected options using their IDs
            else:
                response = Response.objects.create(
                    question=question,
                    response_text=response_text
                )

            responses.append(response)

        return {'responses': responses}


# class BulkResponseSerializer(serializers.Serializer):
#     print(request)
#     responses = ResponseSerializer(many=True)
#
#     def create(self, validated_data):
#         responses_data = validated_data.get('responses', [])
#         responses = []
#
#         for response_data in responses_data:
#             question = response_data.get('question')
#             response_text = response_data.get('response_text')
#             selected_options = response_data.get('selected_options', [])  # Updated field
#
#             response = Response.objects.create(
#                 question=question,
#                 response_text=response_text if question.type in ['short_text', 'long_text', 'email'] else None
#             )
#
#             if question.type == 'choice':
#                 response.selected_options.set(selected_options)
#
#             responses.append(response)
#
#         return {'responses': responses}


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'option_text']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)  # Add choices to the Question serializer

    class Meta:
        model = Question
        fields = ['id', 'text', 'type', 'required', 'description', 'multiple', 'choices']
