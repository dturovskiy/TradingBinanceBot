# Контракти операторського керування (UA)

## 1. Призначення
<!-- parity-key: operator.scope -->

Runtime має операторські surfaces для сповіщень і керування, зокрема Telegram-facing messaging/panel-style взаємодію. Ця сторінка описує стабільні public-safe контракти керування, а не приватний command syntax чи поточний operational state.

## 2. Межа авторизації
<!-- parity-key: operator.auth -->

Дії оператора проходять access-control та authorization checks. Знання назви команди або доступ до message transport саме по собі не надає повноважень, а публічна документація не повинна розкривати credentials, chat identifiers, allowlists або приватну authorization configuration.

## 3. Сповіщення та панелі
<!-- parity-key: operator.notifications -->

Notifications і status/panel surfaces можуть показувати спостереження, health або workflow context авторизованому оператору. Відображення чи підтвердження інформації відокремлене від зміни trading state.

## 4. Класи команд
<!-- parity-key: operator.command-classes -->

На рівні public contract операторські controls можуть охоплювати observation/status, lifecycle або configuration workflows, notifications/panels та явно авторизовані control actions. Точні privileged command strings, recovery procedures і production parameters залишаються приватними.

## 5. Керування не обходить safety gates
<!-- parity-key: operator.non-authority -->

Operator-control surface не повинен непомітно обходити risk, readiness, recovery, evidence або promotion gates. Research evidence не перетворюється на rollout authority лише тому, що воно доступне через операторський інтерфейс.

## 6. Межа публічної безпеки
<!-- parity-key: operator.public-boundary -->

Не публікуйте chat IDs, access-control lists, tokens, точні privileged або recovery commands, поточний runtime state, incident procedures, поточні positions/trades, infrastructure identifiers або production thresholds.

## 7. Пов'язані матеріали

- [Надійність](reliability.md)
- [Логування та артефакти](logging.md)
- [Карта проєкту](../architecture/project_map.md)
