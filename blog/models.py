from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize
from django.core.files.storage import default_storage
import os


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(
        max_length=160,
        blank=True,
        default='',
        verbose_name='Описание (до 160 символов)',
        help_text='Краткое описание для SEO и превью в соцсетях'
    )
    content = RichTextField(config_name='awesome_ckeditor')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    # Основное изображение
    image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/',
        verbose_name='Основное изображение'
    )

    # Автоматически создаваемые миниатюры
    image_thumbnail = ImageSpecField(
        source='image',
        # processors=[ResizeToFill(400, 500)],  # Обрезаем до точных размеров
        processors=[ResizeToFill(100, 100)],  # Обрезаем до точных размеров
        format='JPEG',
        options={'quality': 85}
    )

    image_medium = ImageSpecField(
        source='image',
        processors=[ResizeToFill(808, 606)],
        format='JPEG',
        options={'quality': 85}
    )

    image_social = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1200, 630)],  # Размер для соцсетей
        format='JPEG',
        options={'quality': 90}
    )

    alt = models.CharField(
        max_length=100,  # Увеличим для лучшего SEO
        verbose_name='Alt текст',
        help_text='Описание изображения для SEO и доступности'
    )

    categories = models.ManyToManyField('Category', related_name='posts')
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    order = models.PositiveIntegerField(default=0, db_index=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['order', '-created_on']

    def save(self, *args, **kwargs):
        # Генерация slug
        if not self.slug:
            self.slug = slugify(self.title)

        # Если обновляется изображение, удаляем старые файлы
        if self.pk:
            try:
                old_post = Post.objects.get(pk=self.pk)
                if old_post.image and old_post.image != self.image:
                    self._delete_image_files(old_post.image)
            except Post.DoesNotExist:
                pass

        super(Post, self).save(*args, **kwargs)

    def _delete_image_files(self, image):
        """Удаляет основное изображение и все сгенерированные миниатюры"""
        if image:
            # Удаляем основное изображение
            if default_storage.exists(image.name):
                default_storage.delete(image.name)

            # Удаляем кэшированные миниатюры
            from imagekit.cachefiles import ImageCacheFile
            for field_name in ['image_thumbnail', 'image_medium', 'image_social']:
                try:
                    cachefile = ImageCacheFile(getattr(self, field_name))
                    cachefile.delete()
                except:
                    pass

    def delete(self, *args, **kwargs):
        """При удалении поста удаляем все связанные изображения"""
        if self.image:
            self._delete_image_files(self.image)
        super(Post, self).delete(*args, **kwargs)

    @property
    def thumbnail_url(self):
        """URL миниатюры для использования в шаблонах"""
        if self.image:
            return self.image_thumbnail.url
        return None

    @property
    def medium_url(self):
        """URL среднего размера для использования в шаблонах"""
        if self.image:
            return self.image_medium.url
        return None

    @property
    def social_url(self):
        """URL изображения для соцсетей"""
        if self.image:
            return self.image_social.url
        return None

    def __str__(self):
        return self.title
