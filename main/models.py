from django.db import models
from django.contrib.auth.models import User


class Words(models.Model):
    word_id = models.BigAutoField(primary_key=True)
    english_word = models.CharField('Англійське слово', max_length=255, unique=True)
    translation = models.CharField('Переклад', max_length=255)

    def __str__(self):
        return f'{self.english_word} - {self.translation}'

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"


class Studying(models.Model):
    word = models.ForeignKey(Words, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_learned = models.BooleanField()

    class Meta:
        unique_together = ('word', 'user')

    def __str__(self):
        return f'{self.user}: {self.word}; {self.is_learned}'

