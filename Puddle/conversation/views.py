from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Conversation
from item.models import Item
from .forms import ConversationMessageForm


@login_required
def new_Conversation(request,item_pk):
  item=get_object_or_404(Item,pk=item_pk)

  if item.created_by == request.user:
    return redirect('dashboard:index')
  

  conversation=Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

  if conversation:
    return redirect('conversation:detail', pk=conversation.first().id)
  if request.method == 'POST':
    form=ConversationMessageForm(request.POST)
    if form.is_valid():
      conversation=Conversation.objects.create(item=item)
      conversation.members.add(request.user)
      conversation.members.add(item.created_by)
      conversation.save()

      conversation_message=form.save(commit=False)
      conversation_message.conversation=conversation
      conversation_message.created_by=request.user
      conversation_message.save()

      return redirect('item:details',pk=item_pk)  
    
  else:
    form=ConversationMessageForm()
    return render(request,'conversation/new.html',{
      'form':form
    })

@login_required
def inbox(request):
  conversation=Conversation.objects.filter(members__in=[request.user.id])
  return render(request,'conversation/inbox.html',{
    'conversation':conversation
  })
@login_required
def detail(request, pk):
  conversations=Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

  if request.method == 'POST':
    form=ConversationMessageForm(request.POST)
    if form.is_valid():
      conversations_message=form.save(commit=False)
      conversations_message.conversations=conversations
      conversations_message.created_by=request.user
      conversations_message.save()
      conversations.save()


      return redirect('conversation:detail', pk=pk)
  else:
       form=ConversationMessageForm()  

  return render(request,'conversation/detail.html',{
    'conversations':conversations,
    'form':form
  })





# Create your views here.
