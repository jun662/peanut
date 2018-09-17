// 轮播图 start
$(function () {
    var $li = $(".slider>.img_part>li");
    var count = 0;
    var $slider = $(".slider");
    var $point = $(".point li");
    var $shortcut = $(".shortcut");
    // 依次显示
    function play(){
        // 判断是否为最后一张，如果是最后一张将count改为第一张
        count++;
        if(count === $li.length){
            count = 0;
        }
        if(count > 2){
            $shortcut.addClass("bg_w");
        }else{
            $shortcut.removeClass("bg_w")
        }
        $point.eq(count).addClass("yellow").siblings().removeClass("yellow");
        $li.eq(count).fadeIn(1000).siblings().fadeOut(1000);
    }
    // 鼠标移入移出事件
    $slider.mouseleave(function () {
        t = setInterval(play, 3000);
    });
    $slider.mouseenter(function () {
        clearInterval(t);
    });
    // 左右按钮功能
    $(".arrow-right").click(play);

    $(".arrow-left").click(function () {
        // 判断是否为第一张，如果是第一张，将count改为最后一张
        count--;
        if(count === -1){
            count = $li.length - 1;
        }
        // 修改shortcut部分的颜色
        if(count > 2){
            $shortcut.addClass("bg_w");
        }else{
            $shortcut.removeClass("bg_w")
        }
        $point.eq(count).addClass("yellow").siblings().removeClass("yellow");
        $li.eq(count).fadeIn(1000).siblings().fadeOut(1000);
    });
    $point.click(function () {
        var i = $point.index($(this));
        // 修改shortcut部分的颜色
        if(i > 2){
            $shortcut.addClass("bg_w");
        }else{
            $shortcut.removeClass("bg_w")
        }
        $point.eq(i).addClass("yellow").siblings().removeClass("yellow");
        $li.eq(i).fadeIn(1000).siblings().fadeOut(1000);

    })


});
// 轮播图 end