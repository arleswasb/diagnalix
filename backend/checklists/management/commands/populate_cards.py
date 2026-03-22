from django.core.management.base import BaseCommand
from checklists.models import Category, MedicalCard, ChecklistItem

class Command(BaseCommand):
    help = 'Popula o banco de dados com os cards médicos iniciais.'

    def handle(self, *args, **options):
        self.stdout.write("Iniciando a população do banco de dados com cards...")

        # --- Categoria Padrão ---
        cat_emergencia, _ = Category.objects.get_or_create(name="Procedimentos de Emergência")

        # --- Card 1: Sequência Rápida de Intubação (SRI) ---
        card_sri, created_sri = MedicalCard.objects.get_or_create(
            title="Sequência Rápida de Intubação (SRI)",
            defaults={
                'category': cat_emergencia,
                'description': 'Checklist para o procedimento de Sequência Rápida de Intubação.',
                'image_url': 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?q=80&w=1200&auto=format&fit=crop'
            }
        )
        if created_sri:
            self.stdout.write(self.style.SUCCESS('Card "Sequência Rápida de Intubação (SRI)" criado.'))
            itens_sri = [
                "Preparação (equipamentos, drogas, equipe)",
                "Pré-oxigenação do paciente",
                "Pré-tratamento (se indicado)",
                "Indução e Paralisia",
                "Posicionamento e Intubação",
                "Confirmação da posição do tubo",
                "Cuidados pós-intubação",
            ]
            for i, item_task in enumerate(itens_sri):
                ChecklistItem.objects.create(card=card_sri, task=item_task, order=i + 1)
            self.stdout.write(f'   - {len(itens_sri)} itens de checklist adicionados para SRI.')
        else:
            self.stdout.write('Card "Sequência Rápida de Intubação (SRI)" já existe.')


        # --- Card 2: Algoritmo de Atendimento Cardiovascular de Emergência ---
        card_ace, created_ace = MedicalCard.objects.get_or_create(
            title="Algoritmo de Atendimento Cardiovascular de Emergência",
            defaults={
                'category': cat_emergencia,
                'description': 'Checklist para o Algoritmo de Atendimento Cardiovascular de Emergência.',
                'image_url': 'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?q=80&w=1200&auto=format&fit=crop'
            }
        )
        if created_ace:
            self.stdout.write(self.style.SUCCESS('Card "Algoritmo de Atendimento Cardiovascular de Emergência" criado.'))
            itens_ace = [
                "Avaliação inicial (ABCDE)",
                "Reconhecimento da Parada Cardiorrespiratória (PCR)",
                "Iniciar compressões torácicas de alta qualidade",
                "Garantir via aérea e ventilação",
                "Análise do ritmo cardíaco (desfibrilável ou não)",
                "Administração de drogas conforme algoritmo",
                "Identificar e tratar causas reversíveis (5Hs e 5Ts)",
            ]
            for i, item_task in enumerate(itens_ace):
                ChecklistItem.objects.create(card=card_ace, task=item_task, order=i + 1)
            self.stdout.write(f'   - {len(itens_ace)} itens de checklist adicionados para ACE.')
        else:
            self.stdout.write('Card "Algoritmo de Atendimento Cardiovascular de Emergência" já existe.')

        self.stdout.write(self.style.SUCCESS("\nPopulação de cards concluída!"))
