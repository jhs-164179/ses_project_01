var map = new kakao.maps.Map(document.getElementById('map'), { // 지도를 표시할 div
    center : new kakao.maps.LatLng(35.936, 127.811), // 지도의 중심좌표 
    level : 13 // 지도의 확대 레벨 
});
// 마우스 휠로 확대 축소하는 기능 제거
map.setZoomable(false);

// 지도 타입 변경 기능 추가
var mapTypeControl = new kakao.maps.MapTypeControl();
map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT)

// 지도 줌 기능 추가
var zoomControl = new kakao.maps.ZoomControl();
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT)

// 글자 생성(수도권)
var content_seoul = '<h4><p style="color:black; font-weight:bold; text-align:center;">수도권 50000대(50%)</p></h4>'

var position_q = new kakao.maps.LatLng(37.5447,126.9884)

var customOverlay = new kakao.maps.CustomOverlay({
    position: position_q,
    content: content_seoul,
    
});
customOverlay.setMap(map);

// 글자 생성(전남)
var content_jeon = '<h5><p style="color:black; font-weight:bold; text-align:center;">전라도 18000대(18%)</p></h5>'

var position_j = new kakao.maps.LatLng(35.1506,126.821)

var customOverlay = new kakao.maps.CustomOverlay({
    position: position_j,
    content: content_jeon,
    
});
customOverlay.setMap(map);

// 원 생성(서울)
var circle = new kakao.maps.Circle({
    center: new kakao.maps.LatLng(37.5447,126.9884), // 원 중심 설정
    radius: 50000, // 원 반지름 설정 (단위:미터)
    strokeWeight: 1, // 테두리 선의 굵기 설정
    strokeColor: '#75B8FA', // 테두리 선의 색 설정
    strokeOpacity: 1, // 테두리 선의 투명도 설정
    fillColor: '#75B8FA', // 채우기 색 설정
    fillOpacity: 0.7 // 채우기 투명도 설정
});

circle.setMap(map);

// 원 생성(광주)
var circle2 = new kakao.maps.Circle({
    center: new kakao.maps.LatLng(35.1506,126.821), // 원 중심 설정
    radius: 20000, // 원 반지름 설정 (단위:미터)
    strokeWeight: 1, // 테두리 선의 굵기 설정
    strokeColor: '#DB4455', // 테두리 선의 색 설정
    strokeOpacity: 1, // 테두리 선의 투명도 설정
    fillColor: '#DB4455', // 채우기 색 설정
    fillOpacity: 0.7 // 채우기 투명도 설정
});
circle2.setMap(map);


//=======================================================================================
function chNation() {
    var level = map.getLevel();

    if (level != 13){map.setLevel(13);}

    // 지도의 중심좌표 변경
    var moveLation = new kakao.maps.LatLng(35.936, 127.811);

    // map.setCenter(moveLation)
    map.panTo(moveLation);
}

function chCap() {
    var level = map.getLevel();

    if (level != 11){map.setLevel(11);}
        
     // 지도의 중심좌표 변경
    var moveLation = new kakao.maps.LatLng(37.4789, 126.8763);

    // map.setCenter(moveLation)
    map.panTo(moveLation);
}

function chGang() {
    var level = map.getLevel();

    if (level != 11){map.setLevel(11);}
        
    // 지도의 중심좌표 변경
    var moveLation = new kakao.maps.LatLng(37.6779, 128.5318);

    // map.setCenter(moveLation)
    map.panTo(moveLation);
}

function chChung() {
    var level = map.getLevel();

    if (level != 12){map.setLevel(12);}
        
    // 지도의 중심좌표 변경
    var moveLation = new kakao.maps.LatLng(36.634, 127.1805);

    // map.setCenter(moveLation)
    map.panTo(moveLation);
}

function chJeolla() {			
    var level = map.getLevel();

    if (level != 11){map.setLevel(11);}
        
    // 지도의 중심좌표 변경
    var moveLation = new kakao.maps.LatLng(35.3617, 126.8206);

    // map.setCenter(moveLation)
    map.panTo(moveLation);
}

function chGyeong() {
    var level = map.getLevel();

    if (level != 12){map.setLevel(12);}
        
    // 지도의 중심좌표 변경
    var moveLation = new kakao.maps.LatLng(35.9609, 128.9497);

    // map.setCenter(moveLation)
    map.panTo(moveLation);
}

function chJeju() {
    var level = map.getLevel();

    if (level != 10){map.setLevel(10);}
        
    // 지도의 중심좌표 변경
    var moveLation = new kakao.maps.LatLng(33.3738, 126.547);

    // map.setCenter(moveLation)
    map.panTo(moveLation);
}