from django_components import component


@component.register("card")
class Card(component.Component):
    template_file = "template.html"

    def get_context_data(self, date):
        return {"date": date}
