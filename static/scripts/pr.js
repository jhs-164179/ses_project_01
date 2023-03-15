$(function () {
    $("#sub").on("click", validation);
});

function validation() {
    let chimsoo = $("#chimsoo").val();
    let cctv = $("#cctv").val();
    let search = $("#search").val();
    let elecar_1 = $("#elecar").val();
    let statis_2 = $("#statis_2").val();
    let statis_1 = $("#statis_1").val();
    let pl_mi_1 = $("#updown_1").val();
    let pl_mi_2 = $("#updown_2").val();
    let tour = $("#tour").val();

    console.log(chimsoo);
    console.log(cctv);
    console.log(search);
    console.log(elecar_1);
    console.log(statis_2);
    console.log(statis_1);
    console.log(pl_mi_1);
    console.log(pl_mi_2);
    console.log(tour);

    if (
        !$("#chimsoo").is(":checked") &&
        !$("#cctv").is(":checked") &&
        !$("#search").is(":checked") &&
        !$("#elecar").is(":checked") &&
        !$("#statis_2").is(":checked") &&
        !$("#statis_1").is(":checked") &&
        !$("#updown_1").is(":checked") &&
        !$("#updown_2").is(":checked") &&
        !$("#tour").is(":checked")
    ) {
        alert("한가지 이상의 feature를 선택해야 합니다!");
        return false;
    } else {
        list = []
        for(var i=0;i<9;i++){
            list.push
        }
        console.log("해제");
    }
}
