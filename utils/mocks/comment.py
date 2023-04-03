from faker import Faker

fake = Faker()


def generate_mock_comments(num_comments):
    return [generate_comment(i) for i in range(1, num_comments + 1)]


def generate_comment(id):
    author = {
        "avatarUrl": fake.image_url(),
        "name": fake.name(),
    }
    content = [
        {"text": fake.paragraph()},
    ]
    return {
        "id": id,
        "author": author,
        "content": content,
    }
