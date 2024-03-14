document.addEventListener('DOMContentLoaded', function() {
  const teamInfo = {
    'Brazil': {
        'ranking': '1',
        'name': '巴西',
        'starPlayer': '内马尔，利沙利松，阿利松',
        'coach': '蒂特'
    },
    'Belgium': {
        'ranking': '2',
        'name': '比利时',
        'starPlayer': '凯文·德布劳内，卢卡库',
        'coach': '马丁内斯'
    },
    'Argentina': {
        'ranking': '3',
        'name': '阿根廷',
        'starPlayer': '莱昂内尔·梅西，迪马利亚',
        'coach': '斯卡洛尼'
    },
    'France': {
        'ranking': '4',
        'name': '法国',
        'starPlayer': '基利安·姆巴佩，本泽马',
        'coach': '德尚'
    },
    'England': {
        'ranking': '5',
        'name': '英格兰',
        'starPlayer': '哈里·凯恩，福登',
        'coach': '索斯盖特'
    },
    'Spain': {
        'ranking': '7',
        'name': '西班牙',
        'starPlayer': '塞尔吉奥·布斯克茨，佩德里',
        'coach':'恩里克'
    },
    'Netherlands': {
        'ranking': '8',
        'name': '荷兰',
        'starPlayer': '弗吉尔·范迪克，德佩',
        'coach': '路易斯·范加尔'
    },
    'Portugal': {
        'ranking': '9',
        'name': '葡萄牙',
        'starPlayer': '克里斯蒂亚诺·罗纳尔多，菲利克斯',
        'coach': '桑托斯'
    },
    'Denmark': {
        'ranking': '10',
        'name': '丹麦',
        'starPlayer': '克里斯蒂安·埃里克森，克亚尔',
        'coach': '尤勒曼'
    },
    'Germany': {
        'ranking': '11',
        'name': '德国',
        'starPlayer': '托马斯·穆勒，京多安',
        'coach': '弗里克'
    },
    'Croatia': {
        'ranking': '12',
        'name': '克罗地亚',
        'starPlayer': '卢卡·莫德里奇，佩里西奇',
        'coach': '达利奇'
    },
    'Mexico': {
        'ranking': '13',
        'name': '墨西哥',
        'starPlayer': '赫尔维·洛萨诺，奥乔亚',
        'coach': '马蒂诺'
    },
    'Uruguay': {
        'ranking': '14',
        'name': '乌拉圭',
        'starPlayer': '路易斯·苏亚雷斯，卡瓦尼',
        'coach': '迭戈·阿隆索'
    },
    'Switzerland': {
        'ranking': '15',
        'name': '瑞士',
        'starPlayer': '格兰尼特·扎卡，沙奇里',
        'coach': '穆拉特·雅金'
    },
    'United States': {
        'ranking': '16',
        'name': '美国',
        'starPlayer': '克里斯蒂安·普利西奇，德斯特',
        'coach': '贝尔哈特'
    },
    'Senegal': {
        'ranking': '18',
        'name': '塞内加尔',
        'starPlayer': '库利巴利， 格耶',
        'coach': '阿里乌·西塞'
    },
    'Wales': {
        'ranking': '19',
        'name': '威尔士',
        'starPlayer': '加雷斯·贝尔，拉姆塞',
        'coach': '罗伯特·佩兰'
    },
    'Iran': {
        'ranking': '20',
        'name': '伊朗',
        'starPlayer': '萨达尔·阿兹蒙，塔雷朱',
        'coach': '奎罗斯'
    },
    'Serbia': {
        'ranking': '21',
        'name': '塞尔维亚',
        'starPlayer': '亚历山大·米特罗维奇，塔迪奇',
        'coach': '斯托伊科维奇'
    },
    'Morocco': {
        'ranking': '22',
        'name': '摩洛哥',
        'starPlayer': '哈基姆·齐耶什，阿什拉夫',
        'coach': '雷格拉吉'
    },
    'Japan': {
        'ranking': '24',
        'name': '日本',
        'starPlayer': '南野拓实，富安健洋',
        'coach': '西野朗'
    },
    'Poland': {
        'ranking': '26',
        'name': '波兰',
        'starPlayer': '罗伯特·莱万多夫斯基，泽林斯基',
        'coach': '朱赫涅维奇'
    },
    'South Korea': {
        'ranking': '28',
        'name': '韩国',
        'starPlayer': '孙兴慜，黄喜灿',
        'coach': '保罗·本托'
    },
    'Tunisia': {
        'ranking': '30',
        'name': '突尼斯',
        'starPlayer': '易卜拉欣·穆萨，哈兹里',
        'coach': '卡德里'
    },
    'Costa Rica': {
        'ranking': '31',
        'name': '哥斯达黎加',
        'starPlayer': '凯洛尔·纳瓦斯，坎贝尔',
        'coach': '苏亚雷斯'
    },
    'Australia': {
        'ranking': '38',
        'name': '澳大利亚',
        'starPlayer': '马修·莱基，穆伊',
        'coach': '阿诺德'
    },
    'Canada': {
        'ranking': '41',
        'name': '加拿大',
        'starPlayer': '阿方索·戴维斯',
        'coach': '赫德曼'
    },
    'Cameroon': {
        'ranking': '43',
        'name': '喀麦隆',
        'starPlayer': '服波-莫廷, 奥纳纳',
        'coach': '里格贝特·宋'
    },
    'Ecuador': {
        'ranking': '44',
        'name': '厄瓜多尔',
        'starPlayer': '恩纳尔·瓦伦西亚，莫伊塞斯·凯赛多',
        'coach': '古斯塔沃·阿尔法罗'
    },
    'Saudi Arabia': {
        'ranking': '51',
        'name': '沙特阿拉伯',
        'starPlayer': '法拉赫，沙赫拉尼',
        'coach': '勒纳尔'
    },
    'Qatar': {
        'ranking': '50',
        'name': '卡塔尔',
        'starPlayer': '阿克拉姆·阿菲夫，海多斯',
        'coach': '菲利克斯·桑切斯'
    },
    'Ghana': {
        'ranking': '60',
        'name': '加纳',
        'starPlayer': '安德烈·阿尤，乔丹·阿尤',
        'coach': '奥托·阿多'
    }
};

var matches = [
  ['A', 'Qatar', 'Ecuador', '卡塔尔', '厄瓜多尔'],
  ['A', 'Senegal', 'Netherlands', '塞内加尔', '荷兰'],
  ['A', 'Qatar', 'Senegal', '卡塔尔', '塞内加尔'],
  ['A', 'Netherlands', 'Ecuador', '荷兰', '厄瓜多尔'],
  ['A', 'Ecuador', 'Senegal', '厄瓜多尔', '塞内加尔'],
  ['A', 'Netherlands', 'Qatar', '荷兰', '卡塔尔'],
  ['B', 'England', 'Iran', '英格兰', '伊朗'],
  ['B', 'United States', 'Wales', '美国', '威尔士'],
  ['B', 'Wales', 'Iran', '威尔士', '伊朗'],
  ['B', 'England', 'United States', '英格兰', '美国'],
  ['B', 'Wales', 'England', '威尔士', '英格兰'],
  ['B', 'Iran', 'United States', '伊朗', '美国'],
  ['C', 'Argentina', 'Saudi Arabia', '阿根廷', '沙特阿拉伯'],
  ['C', 'Mexico', 'Poland', '墨西哥', '波兰'],
  ['C', 'Poland', 'Saudi Arabia', '波兰', '沙特阿拉伯'],
  ['C', 'Argentina', 'Mexico', '阿根廷', '墨西哥'],
  ['C', 'Poland', 'Argentina', '波兰', '阿根廷'],
  ['C', 'Saudi Arabia', 'Mexico', '沙特阿拉伯', '墨西哥'],
  ['D', 'Denmark', 'Tunisia', '丹麦', '突尼斯'],
  ['D', 'France', 'Australia', '法国', '澳大利亚'],
  ['D', 'Tunisia', 'Australia', '突尼斯', '澳大利亚'],
  ['D', 'France', 'Denmark', '法国', '丹麦'],
  ['D', 'Australia', 'Denmark', '澳大利亚', '丹麦'],
  ['D', 'Tunisia', 'France', '突尼斯', '法国'],
  ['E', 'Germany', 'Japan', '德国', '日本'],
  ['E', 'Spain', 'Costa Rica', '西班牙', '哥斯达黎加'],
  ['E', 'Japan', 'Costa Rica', '日本', '哥斯达黎加'],
  ['E', 'Spain', 'Germany', '西班牙', '德国'],
  ['E', 'Japan', 'Spain', '日本', '西班牙'],
  ['E', 'Costa Rica', 'Germany', '哥斯达黎加', '德国'],
  ['F', 'Morocco', 'Croatia', '摩洛哥', '克罗地亚'],
  ['F', 'Belgium', 'Canada', '比利时', '加拿大'],
  ['F', 'Belgium', 'Morocco', '比利时', '摩洛哥'],
  ['F', 'Croatia', 'Canada', '克罗地亚', '加拿大'],
  ['F', 'Croatia', 'Belgium', '克罗地亚', '比利时'],
  ['F', 'Canada', 'Morocco', '加拿大', '摩洛哥'],
  ['G', 'Switzerland', 'Cameroon', '瑞士', '喀麦隆'],
  ['G', 'Brazil', 'Serbia', '巴西', '塞尔维亚'],
  ['G', 'Cameroon', 'Serbia', '喀麦隆', '塞尔维亚'],
  ['G', 'Brazil', 'Switzerland', '巴西', '瑞士'],
  ['G', 'Serbia', 'Switzerland', '塞尔维亚', '瑞士'],
  ['G', 'Cameroon', 'Brazil', '喀麦隆', '巴西'],
  ['H', 'Uruguay', 'South Korea', '乌拉圭', '韩国'],
  ['H', 'Portugal', 'Ghana', '葡萄牙', '加纳'],
  ['H', 'South Korea', 'Ghana', '韩国', '加纳'],
  ['H', 'Portugal', 'Uruguay', '葡萄牙', '乌拉圭'],
  ['H', 'Ghana', 'Uruguay', '加纳', '乌拉圭'],
  ['H', 'South Korea', 'Portugal', '韩国', '葡萄牙']
];


  var groupSelect = document.createElement('select');
  groupSelect.id = 'groupSelect';
  groupSelect.name = 'groupSelect';

  var matchSelect = document.createElement('select');
  matchSelect.id = 'matchSelect';
  matchSelect.name = 'matchSelect';

  var groupsContainer = document.getElementById('groupsContainer');
  groupsContainer.appendChild(groupSelect);
  groupsContainer.appendChild(matchSelect);

  var groups = {};
  matches.forEach(function(match) {
    var group = match[0];
    if (!groups[group]) {
      groups[group] = [];
      var groupOption = document.createElement('option');
      groupOption.value = group;
      groupOption.textContent = '小组 ' + group;
      groupSelect.appendChild(groupOption);
    }
    groups[group].push(match);
  });

  groupSelect.addEventListener('change', function() {
    while (matchSelect.firstChild) {
      matchSelect.removeChild(matchSelect.firstChild);
    }

    var selectedGroup = this.value;
    var matches = groups[selectedGroup];
    matches.forEach(function(match) {
      var option = document.createElement('option');
      option.value = match[1] + ' vs ' + match[2]; // 用英文设置值
      option.textContent = match[3] + ' vs ' + match[4]; // 显示中文
      matchSelect.appendChild(option);
    });

    matchSelect.dispatchEvent(new Event('change'));
  });

      matchSelect.addEventListener('change', function() {
        var selectedMatch = this.value.split(' vs ');
        var homeTeamInfo = teamInfo[selectedMatch[0]];
        var awayTeamInfo = teamInfo[selectedMatch[1]];

        var teamInfoContainer = document.getElementById('teamInfoContainer');
        if (!teamInfoContainer) {
            teamInfoContainer = document.createElement('div');
            teamInfoContainer.id = 'teamInfoContainer';
            groupsContainer.appendChild(teamInfoContainer);
        }

    teamInfoContainer.innerHTML = `
        <div class="team-info">
            <h4>主队信息</h4>
            <p><span>球队：</span>${homeTeamInfo.name}</p>
            <p><span>世界排名：</span>${homeTeamInfo.ranking}</p>
            <p><span>明星球员：</span>${homeTeamInfo.starPlayer}</p>
            <p><span>主教练：</span>${homeTeamInfo.coach}</p>
        </div>
        <div class="team-info">
            <h4>客队信息</h4>
            <p><span>球队：</span>${awayTeamInfo.name}</p>
            <p><span>世界排名：</span>${awayTeamInfo.ranking}</p>
            <p><span>明星球员：</span>${awayTeamInfo.starPlayer}</p>
            <p><span>主教练：</span>${awayTeamInfo.coach}</p>
        </div>
    `;

    });


  groupSelect.dispatchEvent(new Event('change'));

});


