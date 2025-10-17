import student_work  # استيراد ملف الطالب
import numbers  # مكتبة للتحقق من الأرقام

# اختبار متغير الاسم


def test_name_variable():
    assert hasattr(
        student_work, 'student_name'), "المتغير student_name غير موجود"
    assert isinstance(student_work.student_name,
                      str), "المتغير student_name يجب أن يكون نصاً (string)"

# اختبار متغير العمر


def test_age_variable():
    assert hasattr(
        student_work, 'student_age'), "المتغير student_age غير موجود"
    assert isinstance(student_work.student_age,
                      int), "المتغير student_age يجب أن يكون رقماً صحيحاً (integer)"
    assert student_work.student_age > 0, "العمر يجب أن يكون رقماً موجباً"

# اختبار متغير المعدل


def test_gpa_variable():
    assert hasattr(student_work, 'gpa'), "المتغير gpa غير موجود"
    assert isinstance(student_work.gpa,
                      numbers.Number), "المتغير gpa يجب أن يكون رقماً"
    assert isinstance(student_work.gpa,
                      float), "المتغير gpa يجب أن يكون رقماً عشرياً (float)"

# اختبار متغير المقررات


def test_courses_variable():
    assert hasattr(student_work, 'courses'), "المتغير courses غير موجود"
    assert isinstance(student_work.courses,
                      list), "المتغير courses يجب أن يكون قائمة (list)"
    assert len(
        student_work.courses) >= 3, "القائمة courses يجب أن تحتوي على 3 مقررات على الأقل"
