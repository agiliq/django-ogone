from django.dispatch import Signal

ogone_payment_accepted = Signal(providing_args=['order_id', \
                                                'amount', 'currency', 'pay_id', 'status', 'ncerror'])
ogone_payment_failed = Signal(providing_args=['order_id', \
                                                'amount', 'currency', 'pay_id', 'status', 'ncerror'])
ogone_payment_cancelled = Signal(providing_args=['order_id', \
                                                'amount', 'currency', 'pay_id', 'status', 'ncerror'])


