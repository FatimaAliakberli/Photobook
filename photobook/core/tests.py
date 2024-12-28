from django.test import TestCase

# Create your tests here.

from .models import Post
from django.core.files.uploadedfile import SimpleUploadedFile

# Create a dummy file
test_image = SimpleUploadedFile(name='test.jpg', content=b'file_content', content_type='image/jpeg')

# Create a Post object
post = Post.objects.create(user='test_user', image=test_image, caption='Test caption')
post.save()

print(post.image.url)  # Should show the correct media URL
