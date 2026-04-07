# Repository Inventory

## 1. 목적

기존 저장소를 adoption하기 전에 먼저 추출해야 하는 사실 목록을 정의한다.

## 2. 최소 inventory 항목

- 언어, 프레임워크, 런타임 버전
- build/test 명령
- 실행/기동 방식
- 환경설정 위치
- DB/cache/queue/broker 의존성
- 외부 연동
- 문서 위치
- 배포 방식
- 운영성 로그/모니터링 포인트
- 위험 구간
  - legacy auth
  - custom build
  - manual SQL
  - undocumented deploy step

## 3. 산출물

- `.agent-base/repository-inventory.json`
- `.agent-base/docs-gap-report.md`
- `.agent-base/role-recommendation.json`

## 4. inventory 질문

- 실제 build/test 명령은 어디에 있는가
- 환경별 profile과 secret은 어디에서 주입되는가
- DB schema와 migration은 누가 소유하는가
- 운영자가 실제로 보는 로그와 health point는 무엇인가
- 배포/롤백 문서는 있는가
- parity가 깨지면 큰 문제가 나는 기능은 무엇인가
