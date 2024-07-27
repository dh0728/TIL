1. 모던 웹 자바스크립트 프레임워크 함께보기 - 임성호

solidJS 랜더링 메커니즘

overview
상위 100프로의 사이트중 45프로의 사이트가 모던 웹 자바스크립트를 프레임워크 활용함
챗봇의 ui도 자바스크립트 프레임워크를 활용함 chatgpt nextjs 제민아이 앵귤러
챗 UI는 100 자바스크립트 프레임워크

자바스크립트 프레임워크 특징
1. 컴포넌트 베이스 
- 재사용가능한 ui

2. 가상 or incremental dom

3. 서버사이드 렌더링(SSR Support)

4. static site generation 

5. typescript support 

최근 트랜드
1. fine-grained Reactivity
- useCallback, useMemo를 사용해서 데이터가 여러번 렌더링 되는 것을 해결

2. partial hydration 

3. server component 

4. image component 

react, 앵귤러, 뷰 기반 트랜드 특징
react

react Compiler : 19부터 적용될 예정
server action 
- client to servver 커뮤니케이션을 가능하게
- use server
- 클라이언트 입력이 바로 서버로 넘어가 보안쪽에서 취약점이 문제로 제기됨
react.dev 
- 개발자 문서가 개편됨
Nextjs
app router
turbopack 
- 개발자에게 빠른 빌드 제공
partial prerendering 
v0
- ai를 사용해서 사용자 인터페이스를 생성 가능, 프레임워크에서 ai를 사용하는 첫번째 사례
next.js.org/learn
- 학습자료 제공

remix
-서버사이드 렌더링을 제공하는 또다른 프레임워크
Remix with Vite
view Transition API
- 부드러운 애니메이션을 보여주는 기능
remix run

solid
Reactive Pimimitives
Reactive primitvies
- createSignal, createEffect

angular
ssr 제공
NgOptimizeDlimage
deferrable views
angular.dev 리뉴얼

vue
perfomanve 향상
vapor Mode
nuxt Devtools
@nuxt/birdge

상태관리의 사실과 오해(flutter) - 김소연, 김마로
클라이언트 사이드 렌더링-브라우저에서 화면을 그림 -spa기반 프레임워크
spa의 문제점: 화면과 데이터를 받는 건 숴워졌으나 상태관리가 어려워짐
Flux가 나오면서 효율이 증가함

상태관리는 어떤 기능들을 할까??
UI 상태관리 라이브러리
Ruverpod이 좀 더 광범위한 기능을 제공
- 상태를 들고 있을 수 있는 객체를 제공(State Holder)
- 상태를 변경하면 상태를 쓰는 곳들(watch)를 전부 변경해주고(observable, memoization)
- 상태 인스턴스를 처음 쓸 때 만들어주고 안쓰면 지워주고(Data Lifecycle Management, DI)
- 하나의 상태를 다른 상태와 결합하거나 활용해서 변신 시킬수 있음
Bloc : dart를 위한 예측 가능한 상태관리 라이브러리
- 상태를 들고 있을 수 있는 객체를 제공(State Holder)
flutter bloc을 쓰면
- 상태를 변경하면 상태를 쓰는 곳들(watch)를 전부 변경해주고(observable)
- 상태 인스턴스의 생명주기를 위젯의 생명주기에 맞추고(Data Lifecycle Management)
- 하나의 상태를 다른 상태와 결합하거나 활용해서 변신 시킬수 있음

### 플러터
플러터는 구글이 출시한 오픈 소스 크로스 플랫폼 GUI 애플리케이션 프레임워크이다. 안드로이드, iOS, 윈도우즈, 리눅스 및 웹용 애플리케이션과 구글 퓨시아용 앱의 주된 소스코드로 사용된다. 






