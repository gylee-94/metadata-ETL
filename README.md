# Metadata ETL Lab

공개 메타데이터 도구를 검토하고, 작은 재현 실험으로 ETL의 데이터 품질과 검증 방법을 공부하는 저장소입니다.

## 현재 범위

- [MetaMuse·LLMDap·MetaHQ 리뷰](reviews/public-metadata-tools.md): 공개 README에서 확인한 기능과 추가 검증 질문.
- [MetaHQ 수록 범위 검증](experiments/metahq-coverage/README.md): 평가 절차와 독립적인 집합 비교 도구.
- [ETL 학습 순서](docs/learning-plan.md): 입력·변환·저장·실패·재실행을 설명하는 연습.
- [설계 판단](docs/design-decisions.md): 평가 단위와 결과 해석의 경계.

현재 테스트는 가상 식별자를 사용한 집합 비교 로직을 검증합니다. MetaHQ 실제 배포본의 수록률이나 세 도구의 추출 정확도를 측정한 결과는 아직 없습니다. 완성된 ETL 제품이나 성능 우위 주장으로 해석하지 않습니다.

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

문서는 공개 출처를 바탕으로 새로 작성했고 테스트 데이터는 가상입니다. 회사 코드, 내부 평가 집합, 미공개 결과, 모델 서버 설정은 포함하지 않습니다. 제3자 코드·논문 전문·DB 배포본은 저장소에 포함하지 않습니다. 자료를 추가할 때에는 출처와 재배포 조건을 별도로 기록합니다.
