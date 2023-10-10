from django import forms

class userform1(forms.Form):
    input1=forms.CharField(label='enter your name',required=False,widget=forms.TextInput({'class':'form-control'}))
    input2=forms.CharField(label='enter your number',required=False,widget=forms.TextInput({'class':'form-control'}))
    email=forms.EmailField(label="Enter Your Email")