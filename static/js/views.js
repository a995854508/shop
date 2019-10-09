// 登录
var login=document.getElementById("login");
var bg=document.getElementById("bg");
var dig=document.getElementById("dig");
var close=document.getElementById("close");
var ok=document.getElementById("ok");
var register=document.getElementById("register")

// 绑定删除按钮的单击事件
login.onclick=function(){
    //显示背景元素和弹框元素
    bg.style.display="block";
    dig.style.display="block";
}
// 绑定确定按钮的单击事件
ok.onclick=function(){
    //隐藏背景元素
    bg.style.display="none";
    //隐藏对话框元素
    dig.style.display="none";
}
close.onclick=function(){
    //隐藏背景元素
    bg.style.display="none";
    //隐藏对话框元素
    dig.style.display="none";
}
login.onmouseover=function(){
        login.style.color="#f00";
        }
login.onmouseout=function(){
        login.style.color="#000";
        }

// 注册
register.onclick=function(){
        window.location.href="./templates/register.html"
        }
register.onmouseover=function(){
        register.style.color="#f00";
        }
register.onmouseout=function(){
        register.style.color="#000";
        }