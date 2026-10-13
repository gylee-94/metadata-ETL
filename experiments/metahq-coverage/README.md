# MetaHQ 수록 범위 검증

상태: **실제 MetaHQ 데이터 검증 미실행**. 현재 제공하는 것은 실험 절차와 가상 데이터로 검증한 집합 비교 도구다. 이 도구는 MetaHQ 전용 파일 파서나 CLI adapter가 아니다.

## 질문

미리 정한 연구 목록에서 검색되지 않는 항목은 질의 조건 때문에 빠졌는가, 사용한 배포본에 없는가?

- target: 사전에 선정한 연구 식별자
- retrieved: 특정 질의가 반환한 연구 식별자
- inventory: 해당 배포본 전체의 연구 식별자

세 집합은 반드시 같은 식별자 단위와 배포 버전을 사용한다. GSM 결과는 출처가 확인된 GSM→GSE 대응으로 변환한 뒤 연구 단위로 비교한다. donor 수와 GSM 수를 직접 비교하지 않는다.

## 실행 절차

1. [선정 기준](study_selection.md)을 먼저 확정한다.
2. [MetaHQ 공식 안내](https://github.com/krishnanlab/meta-hq)에서 도구와 DB를 준비하고 설치 버전·배포 URL·파일 hash를 기록한다.
3. 질의·필터·실행일·원 결과를 저장한다. 현재 버전의 help로 명령을 확인한다.
4. 전체 inventory를 별도로 추출한다. 필터가 적용된 검색 결과를 inventory로 사용하지 않는다. 사용한 파일·열·변환 코드를 기록한다.
5. 식별자를 한 줄에 하나씩 저장한 UTF-8 파일을 만든다. 빈 줄과 중복은 허용하되 각 파일은 동일한 식별자 체계를 사용한다.
6. 아래 도구로 비교한다. raw 파일과 대용량 배포본은 로컬 `runtime/`에 보관한다.

```bash
python3 scripts/compare_coverage.py \
  --target runtime/target.txt \
  --retrieved runtime/retrieved.txt \
  --inventory runtime/inventory.txt > runtime/coverage.json
```

inventory 전체를 확인하지 못했으면 `--inventory`를 생략한다. 이 경우 미조회 항목의 미수록 여부는 `null`로 남긴다. 조회 결과가 inventory에 없는 경우 서로 다른 버전·식별자 또는 불완전한 inventory일 수 있으므로 오류로 중단한다.

## 결과 해석

- `retrieved_targets`: 질의가 반환한 평가 대상.
- `present_but_not_retrieved`: inventory에는 있지만 질의에서 반환되지 않은 대상. 필터·주석 등 원인은 별도 조사한다.
- `absent_from_inventory`: 제출한 전체 inventory에 없는 대상. 다른 버전이나 원 자원에 없다는 뜻은 아니다.
- `query_coverage`: 평가 대상 중 조회된 비율. 추출 정확도나 GEO 전체 recall이 아니다.

출력은 입력 SHA-256을 포함한다. 이는 파일 식별용이며 inventory의 완전성을 보증하지 않는다. 실제 실험 결과를 추가할 때 도구·DB 버전, 선정 근거, 질의, 변환 코드, 제한을 함께 공개한다.
