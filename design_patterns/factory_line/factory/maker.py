from __future__ import annotations

from abc import ABC, abstractmethod

from bottom_sheet.data_models import Context, BottomSheet, Button


class Maker(ABC):
    @abstractmethod
    def make(self, context: Context) -> BottomSheet:
        pass


class HanaReleaseEventMaker(Maker):
    def make(self, context: Context) -> BottomSheet:
        if context.action == 'withdraw':
            buttons = [
                Button(
                    text='출금 신청하기',
                    url=f'self_view/withdraw?account_id={context.account_id}',
                    type='secondary'
                ),
                Button(
                    text='운용 유지하기',
                    url=None,
                    type='primary'
                )
            ]
            return BottomSheet(
                title='하나증권 이벤트 참여하셨네요.',
                message='출금 시 이벤트 대상에서 제외됩니다.',
                highlight=['이벤트 대상'],
                image_url='https://example.com/3QXmQ3E.png',
                buttons=buttons
            )
        elif context.action == 'stop':
            buttons = [
                Button(
                    text='운용 중지하기',
                    url=f'self_view/stop?account_id={context.account_id}',
                    type='secondary'
                ),
                Button(
                    text='운용 유지하기',
                    url=None,
                    type='primary'
                )
            ]
            return BottomSheet(
                title='하나증권 이벤트 참여하셨네요.',
                message='운용 중지시 이벤트 대상에서 제외됩니다.',
                highlight=['이벤트 대상'],
                image_url='https://example.com/3QXmQ3E.png',
                buttons=buttons
            )
        elif context.action =='cancel':
            buttons = [
                Button(
                    text='운용 중지하기',
                    url=f'self_view/stop?account_id={context.account_id}',
                    type='secondary'
                ),
                Button(
                    text='운용 유지하기',
                    url=None,
                    type='primary'
                )
            ]
            return BottomSheet(
                title='하나증권 이벤트 참여하셨네요.',
                message='계약 해지시 이벤트 대상에서 제외됩니다.',
                highlight=['이벤트 대상'],
                image_url='https://example.com/3QXmQ3E.png',
                buttons=buttons,
            )
