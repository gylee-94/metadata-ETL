# Metadata ETL Lab

공개 메타데이터 도구를 검토하고, 작은 재현 실험으로 ETL의 데이터 품질과 검증 방법을 공부하는 저장소입니다.

## 현재 범위

- [MetaMuse·LLMDap·MetaHQ 리뷰](reviews/public-metadata-tools.md): 공개 README에서 확인한 기능과 추가 검증 질문.
- [MetaHQ 수록 범위 검증](experiments/metahq-coverage/README.md): 2026-10-11 실제 조회·수록 여부 검증 기록과 독립적인 집합 비교 도구.
- [ETL 학습 순서](docs/learning-plan.md): 입력·변환·저장·실패·재실행을 설명하는 연습.
- [설계 판단](docs/design-decisions.md): 평가 단위와 결과 해석의 경계.

MetaHQ CLI/core 1.2.0과 데이터 v1.2.0으로 2026-10-11 수행한 검증을 [결과 문서](experiments/metahq-coverage/results_20261011.md)에 정리했습니다. 질환 조회는 359 GSM·7 GSE를 반환했고, 비교한 공개 연구 5건은 해당 조회 및 배포본의 확인한 계층에서 발견되지 않았습니다. 이는 사례 집합의 수록 범위 확인이며, 추출 정확도나 도구 간 성능 우위 평가가 아닙니다.

2026-10-13에는 기존 검증 보고서의 수치를 옮기고 집합 비교를 확인했습니다. MetaHQ를 새로 실행하지 않았으며, 원시 출력과 전체 inventory는 이 저장소에 포함하지 않습니다. 단위 테스트는 가상 식별자로 비교 로직을 검증합니다.

## 실행

Python 3.10 이상, 표준 라이브러리만 사용합니다. 저장소 루트에서:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/compare_coverage.py --help
```

## 구성

```text
reviews/                       공개 도구 리뷰와 출처
experiments/metahq-coverage/    선정 기준과 실험 절차
scripts/compare_coverage.py    조회 결과와 배포본 수록 여부 구분
tests/                        가상 데이터 기반 테스트
docs/                         학습 순서와 설계 판단
```

## 자료의 범위

공개 도구 리뷰와 작성자의 기존 검증 기록에서 공개용으로 정리한 결과를 포함합니다. 사례 목록은 공개 GEO 식별자로 구성하며, 내부 환자 수·분류 라벨·코드·서버 설정은 포함하지 않습니다. 단위 테스트 데이터는 가상입니다. 제3자 코드·논문 전문·DB 배포본은 저장소에 포함하지 않습니다. 자료를 추가할 때에는 출처와 재배포 조건을 별도로 기록합니다.
