from app.schema import Mentor, Mentee, Meeting, Feedback
from data_generators.generators import RandomMentor, RandomMentee, RandomMeeting, RandomMenteeFeedback
from data_generators.data_options import generate_uuid


def test_mentor():
    assert all(Mentor(**vars(RandomMentor())) for _ in range(1000))


def test_mentee():
    assert all(Mentee(**vars(RandomMentee())) for _ in range(1000))


def test_meeting():
    assert all(Meeting(**vars(RandomMeeting(generate_uuid(16), generate_uuid(16)))) for _ in range(1000))


def test_feedback():
    assert all(Feedback(**vars(RandomMenteeFeedback(generate_uuid(16), generate_uuid(16)))) for _ in range(1000))


def test_collections():
    test_mentor()
    test_mentee()
    test_meeting()
    test_feedback()


if __name__ == '__main__':
    test_collections()
