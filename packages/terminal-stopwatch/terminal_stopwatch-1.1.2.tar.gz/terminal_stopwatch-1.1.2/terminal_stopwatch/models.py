"""시간 표시 관련 데이터 모델"""

from dataclasses import dataclass

@dataclass
class TimeDisplay:
    hours: int = 0
    minutes: int = 0
    seconds: int = 0

    @classmethod
    def from_seconds(cls, total_seconds: float) -> 'TimeDisplay':
        total_seconds = int(total_seconds)
        total_minutes = total_seconds // 60
        if total_minutes < 60:
            return cls(
                minutes=total_minutes,
                seconds=total_seconds % 60
            )
        return cls(
            hours=total_minutes // 60,
            minutes=total_minutes % 60,
            seconds=total_seconds % 60
        )

    def __str__(self) -> str:
        if self.hours > 0:
            return f"{self.hours:02d} : {self.minutes:02d} : {self.seconds:02d}"
        return f"{self.minutes:02d} : {self.seconds:02d}" 