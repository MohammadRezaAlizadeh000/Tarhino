from django.shortcuts import render

data_list = [
    {
        'teacher': 'کوثر حیدری',
        'name': 'دوره آموزشی جامع پروژه محور Adobe XD',
        'image': 'adobe-xd-course-thumbnail-400x229.jpg',
    }, {
        'teacher': 'کوثر حیدری',
        'name': 'دوره آموزش طراحی اصولی رابط کاربری(UI)',
        'image': 'adobe-xd-course-thumbnail-400x229.jpg',
    }, {
        'teacher': 'کوثر حیدری',
        'name': 'دوره متخصص تجربه کاربری (UX)',
        'image': 'adobe-xd-course-thumbnail-400x229.jpg',
    }, {
        'teacher': 'کوثر حیدری',
        'name': 'دوره منتورشیپ طراحی UI و UX',
        'image': 'adobe-xd-course-thumbnail-400x229.jpg',
    },
]


def courses_page(request):
    return render(request, 'courses/course_list.html', {'courses': data_list})
