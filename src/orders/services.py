import logging

import stripe

from django.conf import settings

from orders.models import Item, Order

logger = logging.getLogger('StripeService')


class StripeService:
    """Сервис для работы с Stripe"""  # noqa

    def __init__(self, api_key: str = settings.STRIPE_SECRET_KEY):
        if not api_key:
            raise ValueError('API key is not set')
        self.api_key = api_key
        self.client = stripe.StripeClient(api_key)

    def create_session(
        self, item: Item | None = None, order: Order | None = None
    ) -> stripe.checkout.Session:
        """Создание сессии для оплаты"""
        logger.info('Creating session')
        try:
            if not item and not order:
                raise ValueError('Item or order is not set')
            line_items = []
            if item:
                line_items.append(
                    {
                        'price_data': {
                            'currency': item.currency,
                            'product_data': {
                                'name': item.name,
                                'description': item.description,
                                # tax details
                            },
                            'unit_amount': item.price,
                        },
                        'quantity': 1,
                    }
                )
            elif order:
                for itm in order.items.all():
                    line_items.append(
                        {
                            'price_data': {
                                'currency': itm.currency,
                                'product_data': {
                                    'name': itm.name,
                                    'description': itm.description,
                                    # tax details
                                },
                                'unit_amount': itm.price,
                            },
                            'quantity': itm.quantity,
                        }
                    )
            session = self.client.v1.checkout.sessions.create(
                line_items=line_items,
                mode='payment',
                success_url=settings.STRIPE_SUCCESS_URL,
                cancel_url=settings.STRIPE_CANCEL_URL,
            )
            logger.info('Session created')
        except Exception as e:
            logger.error(e)
            raise e
        return session
