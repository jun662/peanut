$(function () {
    /*登陆注册框*/
    var $btn1 = $("#openLogin1");
    var $btn2 = $("#openRegister1");
    var $div1 = $("#login1");
    var $div2 = $("#register1");
    var $close1 = $("#close-button");
    var $close2 = $("#close-button-2");
    var $city = $("#city");
    var $mask = $("#mask");

    $btn1.click(function () {

        /*开启登陆窗口 隐藏注册窗口*/
        $mask.show();
        $div1.show();
        $div2.hide();
    });
    $btn2.click(function () {
        /*开启注册窗口，隐藏登陆窗口*/
        $mask.show();
        $div2.show();
        $div1.hide()
    });
    $close1.click(function () {
        $mask.hide();
        $div1.hide()
    });
    $close2.click(function () {
        $mask.hide();
        $div2.hide()
    });
    /*全部城市显示*/
    $city.mouseenter(function () {
        $city.addClass("active")
    });
    $city.mouseleave(function () {
        $city.removeClass("active")
    });

    /*注册验证*/
    var name =$('#username');
    var email = $('#email');
    var pwd = $('#pwd');
    var re_pwd = $('#re_pwd');
    var flag_error = false;

    name.blur(function(){
        check_name()
    });

    function check_name() {
        var reg =  /^\w{8,16}$/;
        var value = name.val();
        if (value == ""){
            name.next().html('用户名不能为空');
            name.next().show();
            flag_error = true;
            return
        }
        if (reg.test(value)){
            name.next().hide();
            flag_error =false;
        }
        else {
            alert(value);
            name.next().html('由数字字母和下划线组成，字数在8-16位之间');
            name.next().show();
            flag_error
        }
    }

    email.blur(function(){
        check_email()
    });

    function check_email() {
        var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;
        var value = email.val();
        if (value == ""){
            email.next().html('邮箱不能为空');
            email.next().show();
            return
        }
        if (reg.test(value)){
            email.next().hide()
        }
        else{
            email.next().html('请输入正确的邮箱格式');
            email.next().show()
        }
    }

    re_pwd.blur(function(){
        check_pwd()
    });
    pwd.blur(function(){
        check_pwd()
    });

    function check_pwd() {
        var pwd_value = pwd.val();
        var re_pwd_value = re_pwd.val();

        if(pwd_value === ""){
            pwd.next().html("密码不能为空");
            pwd.next().show();
            return
        }
        /*确认密码未填时  不提示错误信息*/
        if(re_pwd_value === ''){
            pwd.next().hide();
            re_pwd.next().hide();
            return
        }
        if (re_pwd_value !== pwd_value){
            re_pwd.next().html("密码输入不一致");
            pwd.next().html("密码输入不一致");
            pwd.next().show();
            re_pwd.next().show();
        }else{
            pwd.next().hide();
            re_pwd.next().hide();
        }
    }
    // 更换验证码图案

});
