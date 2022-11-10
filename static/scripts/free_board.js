window.onload = function() {
    // 페이징에 사용한 모든 a 요소들을 가져와서 변수에 저장.
    let a_list = document.getElementsByClassName('page-link');

    // 위 a 요소들을 반복하면서 클릭 이벤트를 적용.
    Array.from(a_list).forEach(function(e) {
        e.addEventListener('click', function() {
            // 어떤 a 요소에 클릭이 발생하면,
            // 해당 a 요소에 작성된 data-page 속성 값을
            // 검색창 양식 내 input type=hidden에 저장.
            document.getElementById('page').value = this.dataset.page;

            // 검색창 양식을 제출해서 뷰로 전달.
            document.getElementById('searchForm').submit();
        });
    });
}