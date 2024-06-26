from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from courses.forms import CourseModelForm
from courses.models import Course
from operations.models import UserCourse, UserFavorite
from organizations.models import CourseOrg, Teacher
from .forms import RegistrationForm, UserEditForm, ChangePwdForm, TeacherEditForm


class UserEditView(View):
    def get(self, request, *args, **kwargs):
        form = UserEditForm(instance=request.user)
        if request.user.teacher:
            formTeacher = TeacherEditForm(instance=request.user.teacher)
        return render(request, 'userEdit.html', locals())

    def post(self, request, *args, **kwargs):
        form = UserEditForm(request.POST, instance=request.user)
        if request.user.teacher:
            formTeacher = TeacherEditForm(request.POST, instance=request.user.teacher, files=request.FILES)
            if form.is_valid() and formTeacher.is_valid():
                form.save()
                formTeacher.save()

                return redirect('index')
        else:
            if form.is_valid():
                form.save()
                return redirect('index')
        return render(request, 'userEdit.html', locals())


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if not username:
            return render(request, 'login.html', {'错误': '请输入用户名'})
        if not password:
            return render(request, 'login.html', {'错误': '请输入密码'})
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html', {'错误': '用户名或密码错误'})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'register.html', locals())

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'register.html', locals())


class UserCenterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'usercenter.html', locals())


class ChangePasswordView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        pwd_form = ChangePwdForm()
        return render(request, 'ChangePassword.html', locals())

    def post(self, request, *args, **kwargs):
        pwd_form = ChangePwdForm(request.POST)
        if pwd_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            user = request.user
            user.set_password(pwd1)
            user.save()
            return redirect('index')
        else:
            return render(request, 'ChangePassword.html', locals())


class UserCourses(View):
    def get(self, request, *args, **kwargs):
        uc_list = UserCourse.objects.filter(user=request.user)
        courses = [uc.course for uc in uc_list]
        return render(request, 'userCourses.html', locals())


class Delete_course(View):
    def get(self, request, cid, *args, **kwargs):
        if cid:
            UserCourse.objects.filter(course_id=cid, user_id=request.user.id).first().delete()
            return redirect('userCourses')
        return JsonResponse({'status': 'error', 'msg': '删除失败'})


class UserFav(View):
    def get(self, request, *args, **kwargs):
        fav_orgs = UserFavorite.objects.filter(user_id=request.user.id, fav_type=1)
        fav_courses = UserFavorite.objects.filter(user=request.user, fav_type=2)
        fav_orgs = [CourseOrg.objects.filter(id=CFav.fav_id).first() for CFav in fav_orgs]
        fav_courses = [Course.objects.filter(id=OFav.fav_id).first() for OFav in fav_courses]
        return render(request, 'userFav.html', locals())


class DeleteFav(View):
    def get(self, request, fav_id, *args, **kwargs):
        user_fav = get_object_or_404(UserFavorite, fav_id=fav_id, user_id=request.user.id)
        if user_fav:
            user_fav.delete()
            return redirect('userFav')
        return JsonResponse({'status': 'error', 'msg': '删除失败'})


class TeacherZoom(View):
    def get(self, request, *args, **kwargs):
        teacher = Teacher.objects.filter(user_id=request.user.id).first()
        if not teacher:
            return redirect('index')
        name = teacher.name
        # courses = Course.objects.filter(teacher_id=teacher.id).order_by('-add_time', 'status').all()
        courses = Course.objects.filter(teacher_id=teacher.id).order_by('-status', '-add_time').all()
        form = CourseModelForm()
        return render(request, "teacher_zoom.html", locals())

    def post(self, request, *args, **kwargs):
        teacher = Teacher.objects.filter(user_id=request.user.id).first()
        if not teacher:
            return redirect('index')
        form = CourseModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            desc = form.cleaned_data['desc']
            course = Course(name=name, category=category, teacher_id=teacher.id, org_id=teacher.org_id, desc=desc)
            course.save()
        return render(request, "teacher_zoom.html", locals())
