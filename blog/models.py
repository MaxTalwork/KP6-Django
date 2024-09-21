from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name="содержимое", blank=True, null=True)
    preview = models.ImageField(
        upload_to="blog/image",
        blank=True,
        null=True,
        verbose_name="превью (изображение)",
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Дата создания (записи в БД)"
    )
    publication = models.BooleanField(verbose_name="Публикация поста")

    views_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        help_text="Проказывает кол-во просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["title", "slug", "publication"]

    def __str__(self):
        return self.title
