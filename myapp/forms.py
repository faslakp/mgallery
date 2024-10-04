from django import forms


class MovieForm(forms.Form):
    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    options=(
        ("Action","Action"),
        ("Thriller","Thriller"),
        ("Fiction","Fiction"),
    )
    genre=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form-control"}))
    language=forms.CharField()
    year=forms.CharField()
    run_time=forms.IntegerField()
    director=forms.CharField()
    



    # for validation:

    def clean(self):
        cleaned_data=super().clean()


        year=cleaned_data.get("year")

        run_time=cleaned_data.get("run_time")

        if int(year)<1900:
            error_message="year should be>1900"
            self.add_error("year",error_message)

        if run_time<60 or run_time>210:
            error_message="run time should be in between 60 and 210"
            self.add_error("run_time",error_message)