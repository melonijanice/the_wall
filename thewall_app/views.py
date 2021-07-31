from datetime import datetime, timezone
from thewall_app.models import Comment, Message
from login_app.models import User
from django.shortcuts import redirect, render

# Create your views here.
def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context={"User_name":User.objects.get(id=request.session.get('user_id')).first_name,
        "all_comments":Message.objects.all().order_by("-created_at")}
        return render(request,'success.html',context)


def post_message(request):
    this_user=User.objects.get(id=request.session.get('user_id'))
    Message.objects.create(message=request.POST['user_message'],user=this_user)
    return redirect('/wall')

def post_comment(request):
    this_user=User.objects.get(id=request.session.get('user_id'))
    this_message=Message.objects.get(id=request.POST['post_message'])
    Comment.objects.create(comment=request.POST['user_comment'],user=this_user,message=this_message)
    return redirect('/wall')

def delete_message(request):
    if 'delete_message' in request.POST:
        message=Message.objects.get(id=request.POST['message_id'])
        time_delta = datetime.now(timezone.utc) - message.created_at
        if (time_delta.seconds)/60 < 30:
           message.delete()
        return redirect('/wall')
