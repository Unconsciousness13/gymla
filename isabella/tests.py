# from django.test import TestCase
# from django.contrib.auth.models import User
# from isabella.models import Competition, Note, Temporada


# class Test_Create_Competition(TestCase):
#      @classmethod
#      def setUpTestData(cls):
#         test_competition = Competition.objects.create(
#             competition_name='first', location='sofia', club_name='local', competition_date='2022-01-01')
#         print(test_competition)
#         test_temporada = Temporada.objects.create(season='2021')
#         test_note = Note.objects.create(
#             note='12.300', Competition=test_competition.objects.get(id=1) , temporada = test_temporada.objects.get(id=1))
#         testuser = User.objects.create_user(
#             username='testuser', password='testpassword', email='test@example.com')
        
#      def test_isabella_content(self):
#         competition = Competition.objects.get(id=1)
#         temporada = Temporada.objects.get(id=1)
#         note = Note.objects.get(id=1)
#         competition_name = f'{competition.competition_name}'
#         location = f'{competition.location}'
#         club_name = f'{temporada.club_name}'
#         self.assertEqual(competition_name, 'first')
#         self.assertEqual(location, 'sofia')
#         self.assertEqual(club_name, 'local')
#         self.assertEqual(note.note, '12.300')
#         self.assertEqual(str(competition_name), 'first')
#         self.assertEqual(str(note), '12.300')
#         self.assertEqual(str(temporada),'2021')









