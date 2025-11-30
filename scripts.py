from datacenter.models import Schoolkid, Lesson, Commendation, Chastisement, Mark
import random


def search_student(schoolkid_name):
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников с таким именем, уточните запрос.")
        return None
    except Schoolkid.DoesNotExist:
        print("Ученик с таким именем не найден.")
        return None


def create_commendation(schoolkid_name, subject_title):
    child = search_student(schoolkid_name)
    if child is None:
        return

    lessons =  Lesson.objects.filter(
        year_of_study=child.year_of_study,
        group_letter=child.group_letter, 
        subject__title=subject_title
    )

    last_lesson = lessons.order_by("date").last()

    if last_lesson is None:
        print("Урок по этому предмету не найден.")
        return

    praise = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!", "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!"
    ]

    Commendation.objects.create(
        text=random.choice(praise), created=last_lesson.date, 
        schoolkid=child, subject=last_lesson.subject, 
        teacher=last_lesson.teacher
    )


def remove_chastisements(schoolkid_name):
    child = search_student(schoolkid_name)
    if child is None:
        return

    Chastisement.objects.filter(schoolkid=child).delete()


def fix_marks(schoolkid_name):
    child = search_student(schoolkid_name)
    if child is None:
        return

    bad_marks = Mark.objects.filter(schoolkid=child, points__in=[2,3])
    for bad_point in bad_marks:
        bad_point.points = 5
        bad_point.save()
