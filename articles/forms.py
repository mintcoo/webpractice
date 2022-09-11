from django import forms

from articles.models import Article

# class ArticleForm(forms.Form):
    # title = forms.CharField(max_length=10)
    # content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('header', 'title', 'content',)