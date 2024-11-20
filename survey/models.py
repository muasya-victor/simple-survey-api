from django.db import models

class Question(models.Model):
    TYPE_CHOICES = [
        ('short_text', 'Short Text'),
        ('long_text', 'Long Text'),
        ('email', 'Email'),
        ('choice', 'Choice'),
        ('file', 'File'),
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    required = models.BooleanField(default=True)
    text = models.TextField()
    description = models.TextField(null=True, blank=True)
    multiple = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="responses")
    response_text = models.TextField(null=True, blank=True)  # For text responses
    selected_options = models.ManyToManyField(Choice, blank=True)  # For choice questions
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.question.text}"


class Certificate(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='certificates')
    file_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
