const originalDoughnutDraw = Chart.controllers.doughnut.prototype.draw;


//------- 글짜 크기 위치 ---------------------------------------------------------------
Chart.helpers.extend(Chart.controllers.doughnut.prototype, {
draw: function() {
  const chart = this.chart;
  const {
    width,height,ctx,config
  } = chart.chart;
  const {
    datasets
  } = config.data;
  const dataset = datasets[0];
  const datasetData = dataset.data;
  const completed = datasetData[0];
  const text = `${completed}% `;
  let x, y, mid;

  originalDoughnutDraw.apply(this, arguments);

  const fontSize = (height / 150).toFixed(2); //글짜크기 //소수점 2자리까지 표현.
  ctx.font = fontSize + "em Lato, sans-serif";
  ctx.textBaseline = "top";

  x = Math.round((width - ctx.measureText(text).width) / 1.95);
  y = (height / 1.8) - fontSize;   //x,y 좌표값
  ctx.fillStyle = "white"  // 가운데 글자 색상
  ctx.fillText(text, x, y);
  mid = x + ctx.measureText(text).width / 2;
}
});

//------- b-donut 초기그래프 ---------------------------------------------------------------
var context2 = document.getElementById('myChart').getContext('2d');
const plugin = {
  id: 'customCanvasBackgroundColor',
  beforeDraw: (chart, args, options) => {
    const {ctx} = chart;
    ctx.save();
    ctx.globalCompositeOperation = 'destination-over';
    ctx.fillStyle = options.color || '#99ffff';
    ctx.fillRect(0, 0, chart.width, chart.height);
    ctx.restore();
  }
};

let drawchart;



//------- 박스의 값 percent 에 대입 ---------------------------------------------------------------

var config2 
function getValueInText1(){
var percent_value = document.getElementById("d_data").value;
return percent_value
}

//--- b_donut 입력시 변환되는 그래프---------------------------------------------------------------
document.getElementById("set-chart").addEventListener("click", function(){

  percent_value = getValueInText1()
  config2 = {
    type: 'doughnut',
    data: {
      labels: ['Battery',],
      datasets: [{
        label: 'First dataset',
        data: [percent_value, 100 - percent_value],
        backgroundColor: ['#FFD700', '#ededed']
      }]
    },
    options: {
      legend : {
        labels: {
          fontColor: "#FFD700",
          fontSize: 24,
        }
      },
      plugins: {
        customCanvasBackgroundColor: {
          color: 'transparent'
        }
      }
    },
    plugins: [plugin],
  }

  drawchart = new Chart(context2, config2);

})

var context3 = document.getElementById('myChart3').getContext('2d');




//------- 박스의 값 e_percent 에 대입 ---------------------------------------------------------------

function getValueInText2(){
  var percent_value1= document.getElementById("e_data").value;
  return percent_value1
}

var config3 

document.getElementById("set-chart").addEventListener("click", function(){

  percent_value1 = getValueInText2()
  
  config3 = {
    type: 'doughnut',
    data: {
      labels: ['Encoder',],
      datasets: [{
        label: 'First dataset',
        data: [percent_value1, 100 - percent_value1],
        backgroundColor: ['#DAA520', '#ededed']
      }]
    },
    options: {
      legend : {
        labels: {
          fontColor: "#DAA520",
          fontSize: 24,
        }
      },
      plugins: {
        customCanvasBackgroundColor: {
          color: 'transparent'
        }
      }
    },
    plugins: [plugin],
  }

  drawchart = new Chart(context3, config3);
})



// --- c_donut 초기 그래프---------------------------------------------------------------
var context4 = document.getElementById('myChart4').getContext('2d');


// var config4 = {
//   type: 'doughnut',
//   data: {
//     labels: ['Color',],
//     datasets: [{
//       label: 'First dataset',
//       data: [0, 100],
//       backgroundColor: [$("#c_data").val(), '#ededed']
//     }]
//   },
//   options: {
//     legend : {
//       labels: {
//         fontColor: "#DAA520",
//         fontSize: 24,
//       }
//     },
//     plugins: {
//       customCanvasBackgroundColor: {
//         color: 'transparent'
//       }
//     }
//   },
//   plugins: [plugin],
// }
// 
// drawchart = new Chart(context4,config4);

//------- 박스의 값 c_percent 에 대입 ---------------------------------------------------------------
// function getValueInText(){
//   var percent_value1= document.getElementById("c_data").value;
//   return percent_value1
// }

var config4 

document.getElementById("set-chart").addEventListener("click", function(){

  percent_value1 = 100
  
  config4 = {
    type: 'doughnut',
    data: {
      labels: ['Color',],
      datasets: [{
        label: 'First dataset',
        data: [percent_value1],
        backgroundColor: [$("#c_data").val()]
      }]
    },
    options: {
      legend : {
        labels: {
          fontColor: $("#c_data").val(),
          fontSize: 24,
        }
      },
      plugins: {
        customCanvasBackgroundColor: {
          color: 'transparent'
        }
      }
    },
    plugins: [plugin],
  }
  drawchart = new Chart(context4, config4);
})




document.getElementById('del_do_dset').onclick = function(){
  console.log(config2)
	config2.data.datasets.splice(-1,1);
  config3.data.datasets.splice(-1,1);
  config4.data.datasets.splice(-1,1);
	drawchart.update();	//차트 업데이트
	console.log($(".chart-value"))
}

let percent_value_zero1 = 0;
var config5 = {
  type: 'doughnut',
  data: {
    labels: ['Battery',],
    datasets: [{
      label: 'First dataset',
      data: [percent_value_zero1, 100 - percent_value_zero1],
      backgroundColor: ['#FFD700', '#ededed']
    }]
  },
  options: {
    legend : {
      labels: {
        fontColor: "#FFD700",
        fontSize: 24
      }
    },
    plugins: {
      customCanvasBackgroundColor: {
        color: 'transparent'
      }
    }
  },
  plugins: [plugin],
}

drawchart = new Chart(context2,config5);

let percent_value_zero2 = 0;
var config6 = {
  type: 'doughnut',
  data: {
    labels: ['Encoder',],
    datasets: [{
      label: 'First dataset',
      data: [percent_value_zero2, 100 - percent_value_zero2],
      backgroundColor: ['#DAA520', '#ededed']
    }]
  },
  options: {
    legend : {
      labels: {
        fontColor: "#DAA520",
        fontSize: 24
      }
    },
    plugins: {
      customCanvasBackgroundColor: {
        color: 'transparent'
      }
    }
  },
  plugins: [plugin],
}

drawchart = new Chart(context3,config6);

let percent_value_zero3 = 0;
var config7 = {
  type: 'doughnut',
  data: {
    labels: ['Color',],
    datasets: [{
      label: 'First dataset',
      data: [percent_value_zero3, 100 - percent_value_zero3],
      backgroundColor: ['#339933', '#ededed']
    }]
  },
  options: {
    legend : {
      labels: {
        fontColor: "#339933",
        fontSize: 24
      }
    },
    plugins: {
      customCanvasBackgroundColor: {
        color: 'transparent'
      }
    }
  },
  plugins: [plugin],
}

drawchart = new Chart(context4,config7);

