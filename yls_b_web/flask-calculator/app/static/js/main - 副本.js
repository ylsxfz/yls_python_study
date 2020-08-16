$(document).ready(function() {
    var $mainOutput = $('#output');
    var op = '' 
    var num1 = ''

    var clearData = function() {
        op = ''
        num1 = ''
    };

    var clearOutput = function() {
        $mainOutput.html('');
    };

    $('.nums').click(function() {
        op = $op.val()
        num1 = $num1.val()
        num2 = $(this).val() 
        if(num1 == '' && num2 == '.') return; 
        
        if(num1 == '') {
            $mainOutput.html('');
            $mainOutput.append(num2);
        }
        else{
            $mainOutput.append(num2);
        }
        $num1.val(num2)
    });

    $('#clearButton').click(function() {
        $mainOutput.html('0');
        clearData();
    });

    $('#deleteButton').click(function() {
        input = $mainOutput.html()
        if (input != '0') {
            input = input.substring(0, input.length-1)    
            if (input.substring(input.length-1,input.length)==')'){
                input = input.substring(1,input.length-1)
            }
            $mainOutput.html(input);
            if (input == '') {
                clearData();
                $mainOutput.html('0');
            }
        }
    });

    $('.btn-operate').click(function() { //+-*/
    var newOp = $(this).val();
    op = $op.val()
    num1 = $num1.val()
    if(num1 == '') return;

    if((op=='+' || op=='-') && (newOp=='*' || newOp=='/')){ 
        newStr ='('+$mainOutput.html()+')'+ newOp //添加一对括号
    }
    else{
        newStr = $mainOutput.html() + newOp
    }
    $mainOutput.html(newStr)
    $op.val(newOp);
    });


    $('#resultButton').click(function() {
       if ($mainOutput.html() === '' || ('+-*/').indexOf($mainOutput.html()) != -1) return ;
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange=function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                var result = xmlhttp.responseText;
                $mainOutput.html(result);
                $num1.val(result)
                $op.val('')
            }
        }
        xmlhttp.open("POST","api/getresult")
        xmlhttp.setRequestHeader('content-type', 'application/json'); 
        xmlhttp.send(JSON.stringify({'expr':$mainOutput.html()}));
    });
});
