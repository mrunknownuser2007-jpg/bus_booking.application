from pyscript import window,document

def buttonclicked(event):
  print("you have clicked the button")
  print(event)

def dologin(event):
  print("dologin clicked")
  nameob=document.querySelector("#name_field")
  passwordob=document.querySelector("#password_field")
  print("name : ",nameob.value)
  print("password : ",passwordob.value)
  resultob=document.querySelector(".result")
  resultob.innerHTML=f'<h1> your name is {nameob.value} and password is {passwordob.value}'

def buttonclicked1(event):
  print("you have clicked the button")
  print(event)

def buttonclicked2(event):
  print("you have clicked the button")
  print(event)

def buttonclicked3(event):
  print("you have clicked the button")
  print()
  print(event)    
  