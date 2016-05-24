from django import forms


class PortalForm(forms.Form):
    """docstring for PortalForm"""
    dimmension = forms.CharField(label="", max_length=20)
