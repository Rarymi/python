from faker import Faker

fake = Faker()


def generate_mock_posts(num_posts):
    return [generate_post(i) for i in range(1, num_posts + 1)]


def generate_post(id):
    author = {
        "avatarUrl": fake.image_url(),
        "name": fake.name(),
        "role": fake.job(),
    }
    content = [
        {"type": "paragraph", "text": fake.paragraph()},
        {"type": "paragraph", "text": fake.paragraph()},
        {"type": "link", "text": fake.uri()},
    ]
    return {
        "id": id,
        "author": author,
        "content": content,
        # "publishedAt": datetime.fromisoformat("2023-01-03T20:00:00"),
    }
