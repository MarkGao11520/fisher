"""
create by gaowenfeng on 
"""
from app.libs.enums import PendingStatus

__author__ = "gaowenfeng"


class DriftCollection:

    def __init__(self, drifts, current_user_id):
        self.data = []

        self.data = self._parse(drifts, current_user_id)

    def _parse(self, drifts, current_user_id):
        return [DriftViewModel(drift, current_user_id).data for drift in drifts]


class DriftViewModel:

    def __init__(self, drift, current_user_id):
        self.data = {}

        self.data = self._parse(drift, current_user_id)

    @staticmethod
    def requester_or_gifter(drift, current_user_id):
        return 'requester' if current_user_id == drift.requester_id else 'gifter'

    def _parse(self, drift, current_user_id):
        you_are = DriftViewModel.requester_or_gifter(drift, current_user_id)
        pending_status = PendingStatus.pending_str(drift.pending, you_are)
        r = {
            'drift_id': drift.id,
            'you_are': you_are,
            'book_title': drift.book_title,
            'book_author': drift.book_author,
            'book_img': drift.book_img,
            'date': drift.create_datetime.strftime('%Y-%m-%d'),
            'operator': drift.requester_nickname if you_are != 'requester' \
                else drift.gifter_nickname,
            'message': drift.message,
            'address': drift.address,
            'status_str': pending_status,
            'recipient_name': drift.recipient_name,
            'mobile': drift.mobile,
            'status': drift.pending
        }

        return r
