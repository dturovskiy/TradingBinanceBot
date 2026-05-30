# Гайд з Тестування (UA)

Оновлено: 2026-05-30

## 1. Scope

Ця сторінка описує public-safe validation workflows приватної реалізації.
Точні лічильники test modules навмисно не фіксуються у публічній документації,
оскільки вони часто змінюються.

## 2. Runtime Validation

Із кореня приватної реалізації:

```bash
./scripts/testing/run_tests_quick.sh
./scripts/testing/run_tests.sh
```

Використовуйте quick validation під час ітерацій і full suite перед merge або rollout.

## 3. Focus Areas

Перевіряйте tests та evidence для:

- dry-run: відсутність реального Spot або Convert execution;
- SELL-before-BUY ordering;
- config ownership і precedence;
- режимів risk manager та symbol-level containment;
- config/strategy hot reload і restart boundary для API keys;
- detached launcher behavior;
- archive-root loading і same-core replay parity;
- маршрутизації generated outputs до `data/out/<domain>/`.

## 4. Research Validation

Для research workflows використовуйте локальний archive root:

```bash
python tools/analysis/<research-tool>.py --archive-root <archive-root>
```

Результат, який впливає на rollout, має бути відтворюваним зі стабільного archive root
і формувати reviewable baseline-vs-candidate evidence.

## 5. Documentation Validation

Із кореня публічного документаційного репозиторію:

```bash
python3 scripts/docs/check_language_parity.py
bash scripts/docs/validate_links.sh
git diff --check
```

## 6. Generated Outputs

Generated validation outputs мають використовувати domain-specific paths:

```text
data/out/testing/
data/out/benchmark/
data/out/integration/
data/out/readiness/
data/out/audit/
```

Не розміщуйте generated output у `docs/`, якщо це не навмисно підготовлений
human-maintained public document.
