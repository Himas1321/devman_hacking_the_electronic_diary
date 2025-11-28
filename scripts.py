from datacenter.models import Schoolkid, Lesson, Commendation, Chastisement, Mark
import random

def create_commendation(schoolkid_name, subject_title):

    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников с таким именем, уточните запрос.")
        return
    except Schoolkid.DoesNotExist:
        print("Ученик с таким именем не найден.")
        return

    lessons =  Lesson.objects.filter(
        year_of_study=child.year_of_study,
        group_letter=child.group_letter, 
        subject__title=subject_title
    )

    last_lesson = lessons.order_by("date").last()

    praise = [
    "Молодец!", "Отлично!"," Хорошо!",
    "Гораздо лучше, чем я ожидал!", "Ты меня приятно удивил!", 
    "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!", "Сказано здорово – просто и ясно!", 
    "Ты, как всегда, точен!", "Очень хороший ответ!","Талантливо!",
    "Ты сегодня прыгнул выше головы!"
    ]

    Commendation.objects.create(
        text=random.choice(praise), created=last_lesson.date, 
        schoolkid=child, subject=last_lesson.subject, 
        teacher=last_lesson.teacher
    )


def remove_chastisements(schoolkid_name):
    
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников с таким именем, уточните запрос.")
        return
    except Schoolkid.DoesNotExist:
        print("Ученик с таким именем не найден.")
        return

    bad_chastisements = Chastisement.objects.filter(schoolkid=child)
    for bad_chastisement in bad_chastisements:
            bad_chastisement.delete()


def fix_marks(schoolkid_name):

    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников с таким именем, уточните запрос.")
        return
    except Schoolkid.DoesNotExist:
        print("Ученик с таким именем не найден.")
        return

    bad_marks = Mark.objects.filter(schoolkid=child, points__in=[2,3])
    for bad_point in bad_marks:
            bad_point.points = 5
            bad_point.save()