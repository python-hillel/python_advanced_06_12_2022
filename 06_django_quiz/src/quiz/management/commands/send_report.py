from datetime import datetime, time, timedelta

from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware
from prettytable import PrettyTable

from quiz.models import Result


class Command(BaseCommand):
    help = "Send Today's Report to Admins"

    def handle(self, *args, **options):
        start = make_aware(datetime.combine(timezone.now(), time()))
        end = make_aware(datetime.combine(timezone.now() + timedelta(1), time()))

        results = Result.objects.filter(update_timestamp__range=(start, end), state=1)
        # WHERE update_timestamp >= start and update_timestamp <= end

        if results:
            tab = PrettyTable()
            tab.field_names = ['Username', 'Test', 'Correct/Incorrect', 'Points', 'Duration']

            for result in results:
                tab.add_row([
                    result.user.username,
                    result.exam.title,
                    f'{result.num_correct_answers}/{result.num_incorrect_answers}',
                    result.points(),
                    f'{round((result.update_timestamp - result.create_timestamp).total_seconds())}s.'
                ])

            subj = f"Report from {start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}"
            mail_admins(subject=subj, message=tab.get_string(), html_message=tab.get_html_string())
            self.stdout.write("The report was sent by the admin's email.")
        else:
            self.stdout.write("Nothing to send.")
