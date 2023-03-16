from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

class Contact(
    ActivatorModel,
    TitleDescriptionModel,
    Model
):
  class Meta:
    verbose_name_plural = "Contacts"

  email = models.EmailField(verbose_name="Email")

  #string representation of the model
  def __str__(self):
    return f'{self.title}'