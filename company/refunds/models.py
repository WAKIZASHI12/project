from django.db import models
# from tickets.models import Ticket
 
class RefundRequest(models.Model):
    # ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    processed_at = models.DateTimeField(null=True, blank=True)

    def calculate_refund_amount(self):
        # Calculate and return the refund amount
        pass
     # Make sure to import the Ticket model correctly


    # ... other fields and methods ...