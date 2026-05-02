"""
Dữ liệu công thức nấu ăn thật cho hệ thống Food Tracker AI.
"""

REAL_RECIPE_DATA = {
    "Cam": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Nước cam vắt mật ong",
                "ingredients": ["2 quả cam", "1 muỗng mật ong", "Đá viên"],
                "instructions": "1. Cắt đôi quả cam vắt lấy nước.\n2. Thêm mật ong và khuấy đều.\n3. Thêm đá và thưởng thức."
            },
            {
                "recipe_name": "Vịt áp chảo sốt cam",
                "ingredients": ["Ức vịt", "1 quả cam", "Tỏi", "Đường", "Nước mắm"],
                "instructions": "1. Áp chảo ức vịt xém mỡ.\n2. Vắt nước cam, đun lửa nhỏ với đường và mắm đến khi sệt lại.\n3. Rưới sốt lên thịt vịt."
            },
            {
                "recipe_name": "Salad cam chua ngọt",
                "ingredients": ["1 quả cam", "Xà lách", "Cà chua bi", "Dầu giấm"],
                "instructions": "1. Lột vỏ cam, tách từng múi.\n2. Trộn xà lách, cà chua bi.\n3. Rưới dầu giấm và thưởng thức."
            }
        ]
    },
    "Trứng": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Trứng chiên nước mắm",
                "ingredients": ["3 quả trứng", "Nước mắm", "Hành lá", "Đường"],
                "instructions": "1. Đánh tan trứng với gia vị.\n2. Phi thơm hành, đổ trứng vào chiên vàng đều hai mặt."
            },
            {
                "recipe_name": "Trứng ngâm tương Hàn Quốc",
                "ingredients": ["6 quả trứng", "Nước tương", "Hành tây", "Tỏi", "Ớt", "Mè rang"],
                "instructions": "1. Luộc trứng lòng đào (6 phút) rồi bóc vỏ.\n2. Đun hỗn hợp nước tương, đường, nước. Để nguội.\n3. Ngâm trứng cùng hành, tỏi, ớt qua đêm."
            },
            {
                "recipe_name": "Canh cà chua trứng",
                "ingredients": ["2 quả trứng", "2 quả cà chua", "Hành ngò", "Gia vị"],
                "instructions": "1. Xào nhừ cà chua, thêm nước đun sôi.\n2. Đánh tan trứng rưới từ từ vào nồi tạo vân.\n3. Nêm nếm, rắc hành ngò và tắt bếp."
            },
            {
                "recipe_name": "Trứng hấp kiểu Nhật (Chawanmushi)",
                "ingredients": ["2 quả trứng", "200ml nước dashi", "Tôm", "Nấm", "Hành lá"],
                "instructions": "1. Đánh trứng với nước dashi, lọc qua rây.\n2. Cho tôm, nấm vào chén, đổ hỗn hợp trứng.\n3. Hấp lửa nhỏ 15 phút đến khi trứng đông mịn."
            }
        ]
    },
    "Thịt heo": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Thịt kho tàu (thịt kho trứng)",
                "ingredients": ["500g thịt ba chỉ", "4 quả trứng luộc", "Nước dừa tươi", "Nước mắm", "Đường", "Hành tím"],
                "instructions": "1. Cắt thịt miếng vuông, ướp nước mắm, đường.\n2. Rim thịt với nước màu đến khi lên màu cánh gián.\n3. Đổ nước dừa, thêm trứng, kho lửa nhỏ 1.5 tiếng."
            },
            {
                "recipe_name": "Sườn xào chua ngọt",
                "ingredients": ["500g sườn non", "Cà chua", "Dứa", "Hành tây", "Tương cà", "Giấm"],
                "instructions": "1. Chặt sườn miếng vừa, ướp gia vị, chiên vàng.\n2. Xào hành tây, cà chua, dứa. Thêm tương cà, giấm, đường.\n3. Cho sườn vào đảo đều, rim đến khi sốt sệt bám sườn."
            },
            {
                "recipe_name": "Bún thịt nướng",
                "ingredients": ["300g thịt vai/nạc", "Bún tươi", "Rau sống", "Đồ chua", "Nước mắm pha"],
                "instructions": "1. Ướp thịt với sả, tỏi, mắm, đường, dầu hào qua đêm.\n2. Nướng trên bếp than hoặc lò đến khi thơm vàng.\n3. Xếp bún, rau sống, thịt nướng, rưới mắm pha."
            },
            {
                "recipe_name": "Thịt luộc chấm mắm tôm",
                "ingredients": ["500g thịt ba chỉ", "Mắm tôm", "Chanh", "Ớt", "Đường", "Rau sống"],
                "instructions": "1. Luộc thịt với gừng đập dập, vớt bọt.\n2. Thịt chín vớt ra ngâm nước đá cho giòn da.\n3. Thái mỏng, ăn kèm mắm tôm pha chanh ớt đường."
            }
        ]
    },
    "Thịt bò": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Bò lúc lắc",
                "ingredients": ["300g thịt bò thăn", "Tỏi", "Bơ", "Tiêu đen", "Xì dầu", "Cà chua", "Xà lách"],
                "instructions": "1. Cắt bò hạt lựu, ướp tỏi, xì dầu, tiêu, đường.\n2. Phi bơ tỏi, xào bò lửa lớn nhanh tay.\n3. Bày ra đĩa xà lách, cà chua, ăn kèm cơm nóng."
            },
            {
                "recipe_name": "Bò nhúng dấm",
                "ingredients": ["300g bò bắp mỏng", "Giấm gạo", "Sả", "Dứa", "Rau sống cuốn", "Bánh tráng"],
                "instructions": "1. Đun giấm gạo với sả, dứa sôi trong lẩu.\n2. Nhúng từng lát bò vào nồi vài giây.\n3. Cuốn bánh tráng với rau sống, chấm mắm nêm."
            },
            {
                "recipe_name": "Bò xào rau cải",
                "ingredients": ["200g bò thăn", "Cải ngọt", "Tỏi", "Dầu hào", "Tiêu"],
                "instructions": "1. Thái bò mỏng, ướp dầu hào, tiêu, chút bột bắp.\n2. Xào bò lửa lớn nhanh tay, trút ra.\n3. Xào cải ngọt với tỏi, cho bò lại, đảo đều."
            },
            {
                "recipe_name": "Cháo bò bằm",
                "ingredients": ["150g bò bằm", "1 chén gạo", "Hành tím", "Gừng", "Hành lá", "Tiêu"],
                "instructions": "1. Nấu cháo gạo nhuyễn.\n2. Phi hành tím, xào bò bằm với gừng.\n3. Cho bò vào cháo, nêm nếm, rắc hành tiêu."
            }
        ]
    },
    "Thịt gà": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Gà luộc lá chanh",
                "ingredients": ["1 con gà ta", "Lá chanh", "Muối", "Gừng", "Nước mắm gừng"],
                "instructions": "1. Rửa gà, nhồi gừng lá chanh vào bụng.\n2. Luộc nước sôi, lửa nhỏ 25 phút. Ngâm nước đá.\n3. Chặt miếng, ăn kèm muối tiêu chanh hoặc mắm gừng."
            },
            {
                "recipe_name": "Cánh gà chiên nước mắm",
                "ingredients": ["500g cánh gà", "Nước mắm", "Đường", "Tỏi", "Ớt"],
                "instructions": "1. Ướp cánh gà với gia vị 30 phút, chiên giòn vàng.\n2. Rim nước mắm, đường, tỏi đến khi sệt.\n3. Tráng sốt lên cánh gà, rắc mè rang."
            },
            {
                "recipe_name": "Gà kho gừng",
                "ingredients": ["500g đùi gà", "Gừng", "Nước mắm", "Đường", "Tiêu"],
                "instructions": "1. Chặt gà miếng vừa, ướp mắm đường tiêu.\n2. Phi gừng thái sợi, cho gà vào rim.\n3. Kho lửa nhỏ đến khi nước sệt bám đều thịt."
            },
            {
                "recipe_name": "Cơm gà Hội An",
                "ingredients": ["Đùi gà", "Gạo", "Nghệ", "Hành tây", "Rau răm", "Nước mắm pha"],
                "instructions": "1. Luộc gà, lấy nước nấu cơm với nghệ và mỡ gà.\n2. Xé phay thịt gà, trộn hành tây rau răm.\n3. Dọn cơm nghệ, gà xé, chan nước mắm pha."
            }
        ]
    },
    "Tôm": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Tôm rang muối ớt",
                "ingredients": ["300g tôm sú", "Muối", "Ớt bằm", "Tỏi", "Bơ"],
                "instructions": "1. Cắt râu tôm, rửa sạch, để ráo.\n2. Phi tỏi ớt, cho tôm vào xào lửa lớn.\n3. Thêm muối, bơ, đảo nhanh đến khi tôm cong đỏ."
            },
            {
                "recipe_name": "Tôm hấp bia",
                "ingredients": ["500g tôm", "1 lon bia", "Sả", "Gừng", "Muối tiêu chanh"],
                "instructions": "1. Xếp tôm vào nồi, rải sả gừng đập dập.\n2. Đổ bia ngập 1/3, đậy nắp hấp lửa lớn 5 phút.\n3. Vớt tôm ra, chấm muối tiêu chanh."
            },
            {
                "recipe_name": "Tôm sốt bơ tỏi",
                "ingredients": ["300g tôm", "3 muỗng bơ", "Tỏi băm", "Rau mùi tây", "Chanh"],
                "instructions": "1. Bóc vỏ tôm chừa đuôi, ướp muối tiêu.\n2. Tan bơ, phi tỏi vàng, cho tôm vào áp chảo.\n3. Vắt chanh, rắc mùi tây và dọn nóng."
            }
        ]
    },
    "Cá": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Cá kho tộ",
                "ingredients": ["500g cá lóc/cá basa", "Nước mắm", "Đường thắng", "Tiêu", "Hành lá", "Ớt", "Tỏi"],
                "instructions": "1. Cắt cá khúc, ướp mắm, đường, tiêu, tỏi.\n2. Thắng đường cháy trong tộ đất, xếp cá vào.\n3. Kho lửa nhỏ liu riu đến khi mắm sệt bám cá."
            },
            {
                "recipe_name": "Cá chiên giòn sốt cà",
                "ingredients": ["2 con cá rô phi", "Cà chua", "Hành tây", "Tương cà", "Bột chiên giòn"],
                "instructions": "1. Rửa cá, khía thân, ướp muối nghệ. Lăn bột chiên vàng.\n2. Xào cà chua, hành tây với tương cà, nêm chua ngọt.\n3. Rưới sốt lên cá, rắc hành lá."
            },
            {
                "recipe_name": "Canh cá nấu chua",
                "ingredients": ["300g cá lóc", "Me", "Dứa", "Cà chua", "Giá đỗ", "Bạc hà", "Rau ngổ"],
                "instructions": "1. Nấu nước me chua, lọc lấy nước.\n2. Cho dứa, cà chua vào đun sôi, thả cá.\n3. Khi cá chín, thêm giá, bạc hà, rau ngổ. Nêm vừa."
            },
            {
                "recipe_name": "Cá hấp xì dầu",
                "ingredients": ["1 con cá chẽm/diêu hồng", "Xì dầu", "Gừng", "Hành lá", "Dầu mè"],
                "instructions": "1. Rửa cá, khía vài đường, nhồi gừng.\n2. Hấp cá 12 phút đến khi chín.\n3. Rưới xì dầu, dầu mè nóng, rắc hành gừng thái sợi."
            }
        ]
    },
    "Cà chua": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Sốt cà chua nấu mì Ý",
                "ingredients": ["4 quả cà chua", "Tỏi", "Hành tây", "Dầu ô liu", "Húng quế", "Mì spaghetti"],
                "instructions": "1. Chần cà chua, lột vỏ, xay nhuyễn.\n2. Phi tỏi hành với dầu ô liu, đổ cà chua vào rim.\n3. Nêm gia vị, thêm húng quế, trộn với mì luộc."
            },
            {
                "recipe_name": "Canh cà chua thịt bằm",
                "ingredients": ["3 quả cà chua", "100g thịt bằm", "Hành lá", "Gia vị"],
                "instructions": "1. Xào thịt bằm với hành tím, thêm cà chua bổ múi.\n2. Đổ nước, đun sôi, nêm nếm.\n3. Rắc hành lá, dọn kèm cơm nóng."
            },
            {
                "recipe_name": "Trứng chưng cà chua",
                "ingredients": ["3 quả cà chua", "3 quả trứng", "Hành lá", "Nước mắm", "Đường"],
                "instructions": "1. Bổ múi cà chua, xào mềm với chút đường.\n2. Đập trứng đánh tan, đổ vào chảo cà chua.\n3. Đảo nhẹ đến khi trứng vừa chín tới, rắc hành."
            }
        ]
    },
    "Phở": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Phở bò truyền thống Hà Nội",
                "ingredients": ["Xương ống bò", "Bắp bò", "Gầu bò", "Bánh phở", "Hành tây", "Gừng nướng", "Hoa hồi", "Quế", "Thảo quả"],
                "instructions": "1. Ninh xương bò 4-5 tiếng, vớt bọt kỹ.\n2. Nướng hành tây, gừng. Rang hoa hồi, quế, thảo quả cho vào túi gia vị.\n3. Trụng bánh phở, xếp thịt thái mỏng, chan nước dùng nóng."
            },
            {
                "recipe_name": "Phở gà Sài Gòn",
                "ingredients": ["1 con gà ta", "Bánh phở", "Hành tây", "Giá đỗ", "Rau thơm", "Tương đen", "Tương ớt"],
                "instructions": "1. Luộc gà nguyên con, lấy nước nấu nước dùng.\n2. Xé phay thịt gà.\n3. Trụng phở, xếp gà, chan nước dùng, ăn kèm giá, rau, tương."
            },
            {
                "recipe_name": "Phở xào bò rau cải",
                "ingredients": ["200g bánh phở", "200g bò thái lát", "Cải ngọt", "Giá đỗ", "Hành tây", "Xì dầu"],
                "instructions": "1. Xào bò lửa lớn nhanh tay, trút ra.\n2. Xào hành tây, cải, giá. Cho phở vào đảo.\n3. Thêm bò, nêm xì dầu, dầu hào, đảo đều."
            }
        ]
    },
    "Bún bò Huế": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Bún bò Huế chuẩn vị",
                "ingredients": ["Bắp bò", "Giò heo", "Mắm ruốc", "Sả", "Ớt bột", "Bún sợi to", "Rau sống"],
                "instructions": "1. Hầm xương, bắp bò, giò heo 3 tiếng với sả đập.\n2. Phi dầu điều với ớt bột, sả băm tạo sa tế. Nêm mắm ruốc.\n3. Xếp bún, thịt, giò ra tô, chan nước lèo nóng."
            },
            {
                "recipe_name": "Bún bò chay thanh đạm",
                "ingredients": ["Nấm đùi gà", "Đậu hũ", "Dứa", "Sả", "Mắm chay", "Bún"],
                "instructions": "1. Hầm nước dùng từ rau củ, dứa, sả.\n2. Xào nấm và đậu hũ với sa tế sả.\n3. Trình bày bún ra tô, chan nước dùng chay."
            },
            {
                "recipe_name": "Bún bò Huế tô nhanh (dùng gói gia vị)",
                "ingredients": ["Thịt bò thái", "1 gói gia vị bún bò", "Bún tươi", "Chả Huế", "Rau sống"],
                "instructions": "1. Đun nước sôi, cho gói gia vị vào hòa tan.\n2. Thả bò và chả vào nấu chín.\n3. Cho bún ra tô, chan nước, ăn kèm rau sống."
            }
        ]
    },
    "Cơm tấm": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Cơm tấm sườn bì chả",
                "ingredients": ["Cơm tấm", "Sườn heo", "Bì heo", "Chả trứng", "Mỡ hành", "Nước mắm pha", "Đồ chua"],
                "instructions": "1. Ướp sườn với sả, tỏi, nước mắm, mật ong. Nướng vàng.\n2. Trộn bì với thính gạo.\n3. Xếp cơm tấm, sườn, bì, chả. Rưới mỡ hành, ăn kèm đồ chua."
            },
            {
                "recipe_name": "Cơm tấm gà nướng",
                "ingredients": ["Cơm tấm", "Đùi gà rút xương", "Sả", "Mật ong", "Nước mắm pha"],
                "instructions": "1. Ướp đùi gà với sả băm, mật ong, gia vị.\n2. Nướng lò 200°C 25 phút đến vàng giòn.\n3. Dọn kèm cơm tấm, đồ chua, dưa leo."
            },
            {
                "recipe_name": "Cơm tấm chay",
                "ingredients": ["Cơm tấm", "Sườn chay (từ đậu nành)", "Bì chay", "Chả chay", "Nước tương pha"],
                "instructions": "1. Ướp sườn chay với xì dầu, đường, dầu hào chay, áp chảo.\n2. Trộn bì chay với thính.\n3. Bày cơm, sườn, bì, chả chay, rưới nước tương."
            }
        ]
    },
    "Bánh mì": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Bánh mì thịt nguội Sài Gòn",
                "ingredients": ["Ổ bánh mì", "Chả lụa", "Jambon", "Pa-tê", "Đồ chua", "Dưa leo", "Ngò", "Ớt", "Nước tương"],
                "instructions": "1. Nướng giòn ổ bánh mì, xẻ dọc.\n2. Phết pa-tê, xếp chả lụa, jambon.\n3. Thêm đồ chua, dưa leo, ngò, ớt."
            },
            {
                "recipe_name": "Bánh mì bò kho",
                "ingredients": ["Ổ bánh mì", "300g bắp bò", "Cà rốt", "Sả", "Gừng", "Bột cà ri"],
                "instructions": "1. Ướp bò với bột cà ri, sả, gừng. Xào sơ.\n2. Hầm bò với cà rốt trong nước dùng 2 tiếng.\n3. Nướng bánh mì giòn, chấm nước bò kho."
            },
            {
                "recipe_name": "Bánh mì ốp la",
                "ingredients": ["Ổ bánh mì", "2 quả trứng", "Xì dầu", "Đồ chua", "Ớt"],
                "instructions": "1. Chiên trứng ốp la, nêm xì dầu.\n2. Nướng bánh mì giòn, xẻ dọc.\n3. Kẹp trứng, đồ chua, ớt và thưởng thức."
            },
            {
                "recipe_name": "Bánh mì chả cá Nha Trang",
                "ingredients": ["Ổ bánh mì", "Chả cá chiên", "Xoài xanh bào sợi", "Nước mắm pha", "Rau răm"],
                "instructions": "1. Chiên chả cá vàng giòn, thái lát.\n2. Xẻ bánh mì, xếp chả cá vào.\n3. Thêm xoài bào, rau răm, rưới nước mắm pha."
            }
        ]
    },
    "Bánh xèo": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Bánh xèo miền Nam giòn rụm",
                "ingredients": ["Bột gạo", "Nước cốt dừa", "Bột nghệ", "Tôm", "Thịt heo", "Giá đỗ", "Rau sống"],
                "instructions": "1. Pha bột gạo với nước cốt dừa, nghệ, để nghỉ 30 phút.\n2. Tráng bột mỏng, xếp tôm thịt giá đỗ, gập đôi chiên giòn.\n3. Cuốn rau sống, chấm nước mắm chua ngọt."
            },
            {
                "recipe_name": "Bánh xèo miền Trung",
                "ingredients": ["Bột gạo", "Bột nghệ", "Tôm nhỏ", "Giá đỗ", "Hành lá", "Nước mắm nêm"],
                "instructions": "1. Pha bột lỏng hơn phiên bản miền Nam.\n2. Đổ bánh nhỏ, mỏng. Cho tôm hành.\n3. Cuốn bánh tráng, rau sống, chấm nước mắm nêm Đà Nẵng."
            },
            {
                "recipe_name": "Bánh xèo chay",
                "ingredients": ["Bột gạo", "Nước cốt dừa", "Nghệ", "Đậu hũ", "Nấm", "Giá đỗ", "Rau sống"],
                "instructions": "1. Pha bột với nước cốt dừa, nghệ.\n2. Xào đậu hũ và nấm với gia vị, cho vào bánh.\n3. Chiên giòn, ăn kèm rau sống và nước tương pha."
            }
        ]
    },
    "Bún chả": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Bún chả Hà Nội",
                "ingredients": ["Thịt ba chỉ", "Thịt nạc vai xay", "Bún", "Nước mắm", "Đường", "Giấm", "Đu đủ xanh", "Cà rốt", "Rau sống"],
                "instructions": "1. Thái thịt ba chỉ mỏng, ướp mắm đường, nướng than.\n2. Viên thịt xay tròn, nướng vàng thơm.\n3. Pha nước chấm chua ngọt, cho thịt vào. Ăn kèm bún, rau."
            },
            {
                "recipe_name": "Bún chả Obama (kiểu Hà Nội đặc biệt)",
                "ingredients": ["Thịt ba chỉ", "Nem cua bể", "Bún", "Nước chấm", "Rau sống", "Ớt tỏi"],
                "instructions": "1. Nướng thịt ba chỉ ướp trên bếp than.\n2. Chiên nem cua bể giòn vàng.\n3. Dọn bún, nước chấm riêng, thêm nem và thịt nướng."
            },
            {
                "recipe_name": "Bún chả cá Đà Nẵng",
                "ingredients": ["Chả cá", "Bún", "Nước dùng cá", "Rau sống", "Nước mắm pha"],
                "instructions": "1. Hầm xương cá lấy nước dùng ngọt.\n2. Chiên chả cá vàng, thái lát.\n3. Trụng bún, chan nước dùng, xếp chả cá, ăn kèm rau."
            }
        ]
    },
    "Bún riêu": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Bún riêu cua đồng",
                "ingredients": ["Cua đồng", "Cà chua", "Mắm tôm", "Đậu hũ chiên", "Bún", "Rau sống", "Giấm bỗng"],
                "instructions": "1. Xay cua lọc lấy nước, đun sôi để riêu nổi.\n2. Xào cà chua nhừ, thêm nước cua, nêm mắm tôm.\n3. Chan nước dùng lên bún, thêm riêu, đậu hũ, rau."
            },
            {
                "recipe_name": "Bún riêu chay",
                "ingredients": ["Đậu hũ non", "Cà chua", "Nấm rơm", "Bún", "Rau muống", "Giá đỗ"],
                "instructions": "1. Nghiền đậu hũ non tạo hình giống riêu.\n2. Nấu nước dùng rau củ với cà chua.\n3. Cho riêu đậu hũ vào, ăn kèm bún và rau."
            },
            {
                "recipe_name": "Bún riêu tôm thịt",
                "ingredients": ["Tôm khô", "Thịt heo xay", "Trứng", "Cà chua", "Bún", "Rau sống"],
                "instructions": "1. Xay tôm khô, trộn thịt xay và trứng thành hỗn hợp riêu.\n2. Nấu nước dùng xương heo với cà chua.\n3. Múc riêu cho vào nồi, chan bún, ăn kèm rau."
            }
        ]
    },
    "Gỏi cuốn": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Gỏi cuốn tôm thịt",
                "ingredients": ["Tôm luộc", "Thịt ba chỉ luộc", "Bún", "Rau sống", "Bánh tráng", "Tương hoisin", "Đậu phộng"],
                "instructions": "1. Luộc tôm, thịt. Thái mỏng.\n2. Nhúng bánh tráng nước, xếp rau, bún, tôm thịt, cuốn chặt.\n3. Chấm tương hoisin pha đậu phộng giã."
            },
            {
                "recipe_name": "Gỏi cuốn chay",
                "ingredients": ["Đậu hũ chiên", "Bún", "Xà lách", "Rau thơm", "Dưa leo", "Bánh tráng"],
                "instructions": "1. Chiên đậu hũ vàng, thái thanh.\n2. Nhúng bánh tráng, cuốn rau, bún, đậu hũ.\n3. Chấm nước tương pha tỏi ớt."
            },
            {
                "recipe_name": "Gỏi cuốn bò nướng lá lốt",
                "ingredients": ["Thịt bò xay", "Lá lốt", "Bún", "Rau sống", "Bánh tráng", "Nước mắm pha"],
                "instructions": "1. Ướp bò xay gia vị, cuốn lá lốt nướng than.\n2. Nhúng bánh tráng, xếp rau, bún, bò lá lốt.\n3. Cuốn chặt, chấm nước mắm chua ngọt."
            }
        ]
    },
    "Lẩu": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Lẩu Thái Tom Yum",
                "ingredients": ["Tôm", "Nấm", "Cà chua", "Sả", "Lá chanh", "Ớt hiểm", "Nước cốt dừa", "Sa tế"],
                "instructions": "1. Nấu nước dùng với sả, lá chanh, ớt, cà chua.\n2. Nêm sa tế, nước cốt dừa, mắm.\n3. Nhúng tôm, nấm, rau, bún hoặc mì."
            },
            {
                "recipe_name": "Lẩu gà lá é",
                "ingredients": ["1 con gà ta", "Lá é", "Sả", "Gừng", "Rau nhúng các loại", "Bún/mì"],
                "instructions": "1. Chặt gà, xào sả gừng lấy mùi.\n2. Đổ nước hầm gà, nêm nếm.\n3. Thả lá é vào khi sôi, nhúng rau và bún."
            },
            {
                "recipe_name": "Lẩu mắm miền Tây",
                "ingredients": ["Mắm cá linh/cá sặc", "Cá lóc", "Tôm", "Mực", "Bông bí", "Rau đắng", "Bún"],
                "instructions": "1. Nấu mắm với nước, lọc bỏ xác, nêm đường.\n2. Cho cá, tôm, mực vào nồi khi nước sôi.\n3. Nhúng rau đắng, bông bí, bông súng. Ăn với bún."
            }
        ]
    },
    "Cơm": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Cơm chiên Dương Châu",
                "ingredients": ["Cơm nguội", "Trứng", "Lạp xưởng", "Tôm", "Đậu hà lan", "Cà rốt", "Hành lá"],
                "instructions": "1. Xào trứng sơ, trút ra.\n2. Xào lạp xưởng, tôm, cà rốt, đậu.\n3. Cho cơm nguội vào đảo lửa lớn, thêm trứng, nêm xì dầu."
            },
            {
                "recipe_name": "Cơm gà xối mỡ",
                "ingredients": ["Đùi gà", "Cơm nóng", "Mỡ hành", "Nước mắm tỏi ớt"],
                "instructions": "1. Ướp đùi gà gia vị, chiên giòn vàng.\n2. Chặt gà, xếp lên cơm nóng.\n3. Xối mỡ hành nóng, ăn kèm nước mắm tỏi ớt."
            },
            {
                "recipe_name": "Cơm trộn Hàn Quốc (Bibimbap)",
                "ingredients": ["Cơm", "Bò xào", "Rau bina", "Cà rốt", "Giá đỗ", "Kim chi", "Trứng ốp la", "Tương ớt Gochujang"],
                "instructions": "1. Xào riêng từng loại rau với dầu mè.\n2. Xào bò với xì dầu tỏi.\n3. Bày cơm giữa, xếp rau, bò xung quanh, trứng trên, tương ớt."
            }
        ]
    },
    "Bánh cuốn": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Bánh cuốn Thanh Trì",
                "ingredients": ["Bột gạo", "Bột năng", "Thịt heo xay", "Mộc nhĩ", "Hành khô", "Nước mắm pha"],
                "instructions": "1. Pha bột gạo lỏng, tráng trên vải mỏng hấp chín.\n2. Xào nhân thịt với mộc nhĩ, hành.\n3. Cuốn nhân vào bánh, ăn kèm chả quế và nước mắm pha."
            },
            {
                "recipe_name": "Bánh cuốn trứng",
                "ingredients": ["Bột gạo", "Trứng gà", "Hành phi", "Nước mắm pha", "Rau sống"],
                "instructions": "1. Tráng bột, đập trứng lên mặt bánh khi còn hơi.\n2. Hấp chín, cuộn lại.\n3. Rắc hành phi, ăn kèm nước mắm."
            },
            {
                "recipe_name": "Bánh cuốn chay nhân nấm",
                "ingredients": ["Bột gạo", "Nấm mèo", "Nấm hương", "Đậu hũ", "Nước tương pha"],
                "instructions": "1. Tráng bột mỏng trên vải.\n2. Xào nhân nấm, đậu hũ nghiền.\n3. Cuốn nhân, ăn kèm nước tương pha gừng."
            }
        ]
    },
    "Hủ tiếu": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Hủ tiếu Nam Vang",
                "ingredients": ["Hủ tiếu sợi", "Thịt heo bằm", "Tôm", "Gan heo", "Giá đỗ", "Hẹ", "Hành phi", "Nước dùng xương"],
                "instructions": "1. Ninh xương heo lấy nước dùng trong.\n2. Trụng hủ tiếu, xếp thịt bằm, tôm, gan.\n3. Chan nước dùng, rắc hành phi, hẹ cắt."
            },
            {
                "recipe_name": "Hủ tiếu xào hải sản",
                "ingredients": ["Hủ tiếu sợi", "Tôm", "Mực", "Cải ngọt", "Cà rốt", "Xì dầu"],
                "instructions": "1. Xào tôm mực lửa lớn, trút ra.\n2. Xào rau cải, cà rốt.\n3. Cho hủ tiếu vào đảo, thêm hải sản, nêm xì dầu."
            },
            {
                "recipe_name": "Hủ tiếu khô Mỹ Tho",
                "ingredients": ["Hủ tiếu Mỹ Tho", "Thịt heo", "Tôm", "Gan", "Nước lèo riêng", "Hành phi", "Tương đen"],
                "instructions": "1. Trụng hủ tiếu, trộn tương đen, mỡ hành.\n2. Xếp thịt, tôm, gan lên trên.\n3. Ăn kèm tô nước lèo xương heo riêng."
            }
        ]
    },
    "Rau": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Rau muống xào tỏi",
                "ingredients": ["1 bó rau muống", "5 tép tỏi", "Dầu ăn", "Nước mắm", "Đường"],
                "instructions": "1. Nhặt rau, rửa sạch, cắt khúc.\n2. Phi tỏi vàng thơm, cho rau vào xào lửa lớn.\n3. Nêm mắm đường, đảo nhanh tay để rau giòn xanh."
            },
            {
                "recipe_name": "Canh rau ngót thịt bằm",
                "ingredients": ["Rau ngót", "100g thịt heo bằm", "Gia vị"],
                "instructions": "1. Nhặt lá rau ngót, rửa sạch.\n2. Đun nước sôi, cho thịt bằm vào, vớt bọt.\n3. Thả rau ngót, nêm nếm, đun sôi lại và tắt bếp."
            },
            {
                "recipe_name": "Salad rau trộn dầu giấm",
                "ingredients": ["Xà lách", "Rau rocket", "Cà chua bi", "Dưa leo", "Dầu ô liu", "Giấm táo"],
                "instructions": "1. Rửa sạch các loại rau, để ráo.\n2. Pha dầu ô liu, giấm táo, muối, tiêu.\n3. Trộn rau với sốt dầu giấm ngay trước khi ăn."
            }
        ]
    },
    "Nấm": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Nấm xào bơ tỏi",
                "ingredients": ["200g nấm (đùi gà, kim châm)", "Bơ", "Tỏi", "Rau mùi tây", "Tiêu"],
                "instructions": "1. Rửa nấm, thái lát vừa.\n2. Tan bơ, phi tỏi vàng, cho nấm xào lửa lớn.\n3. Nêm muối tiêu, rắc mùi tây."
            },
            {
                "recipe_name": "Súp nấm kem",
                "ingredients": ["300g nấm hỗn hợp", "Kem tươi", "Hành tây", "Bơ", "Bột mì", "Nước dùng gà"],
                "instructions": "1. Xào hành tây với bơ, thêm nấm xào mềm.\n2. Thêm bột mì, khuấy đều, đổ nước dùng.\n3. Xay nhuyễn, cho kem tươi, đun sôi nhẹ."
            },
            {
                "recipe_name": "Lẩu nấm chay",
                "ingredients": ["Nấm đùi gà", "Nấm kim châm", "Nấm hải sản", "Đậu hũ", "Rau cải", "Bún"],
                "instructions": "1. Nấu nước dùng từ nấm hương khô và rau củ.\n2. Xếp các loại nấm, đậu hũ ra đĩa.\n3. Nhúng nấm, rau, bún vào nồi lẩu."
            }
        ]
    },
    "Đậu hũ": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Đậu hũ sốt cà chua",
                "ingredients": ["2 bìa đậu hũ", "Cà chua", "Hành lá", "Nước mắm", "Đường"],
                "instructions": "1. Cắt đậu hũ miếng vuông, chiên vàng.\n2. Xào cà chua nhừ, nêm mắm đường.\n3. Cho đậu hũ vào rim, rắc hành lá."
            },
            {
                "recipe_name": "Đậu hũ nhồi thịt hấp",
                "ingredients": ["Đậu hũ", "Thịt heo xay", "Mộc nhĩ", "Hành", "Nước mắm"],
                "instructions": "1. Khoét giữa đậu hũ, nhồi thịt xay trộn mộc nhĩ.\n2. Hấp 15 phút đến khi thịt chín.\n3. Rưới nước mắm pha, rắc hành phi."
            },
            {
                "recipe_name": "Đậu hũ Tứ Xuyên (Mapo Tofu)",
                "ingredients": ["Đậu hũ non", "Thịt heo bằm", "Tương đậu Tứ Xuyên", "Tỏi", "Gừng", "Hành lá", "Tiêu Tứ Xuyên"],
                "instructions": "1. Cắt đậu hũ non hạt lựu, trụng nước sôi.\n2. Xào thịt bằm với tỏi gừng, thêm tương đậu.\n3. Cho đậu hũ vào rim nhẹ, rắc tiêu Tứ Xuyên, hành lá."
            }
        ]
    },
    "Cà rốt": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Nước ép cà rốt cam",
                "ingredients": ["2 củ cà rốt", "1 quả cam", "Mật ong", "Đá viên"],
                "instructions": "1. Gọt vỏ cà rốt, cắt khúc.\n2. Ép cà rốt và cam chung.\n3. Thêm mật ong, đá viên."
            },
            {
                "recipe_name": "Cà rốt xào trứng",
                "ingredients": ["2 củ cà rốt", "3 quả trứng", "Hành lá", "Gia vị"],
                "instructions": "1. Bào cà rốt sợi, xào sơ với dầu.\n2. Đập trứng đánh tan, đổ vào chảo cà rốt.\n3. Đảo đều đến khi trứng chín, rắc hành."
            },
            {
                "recipe_name": "Đồ chua (cà rốt củ cải ngâm)",
                "ingredients": ["1 củ cà rốt", "1 củ cải trắng", "Giấm", "Đường", "Muối"],
                "instructions": "1. Bào sợi cà rốt và củ cải, rắc muối vắt ráo.\n2. Pha giấm, đường, nước ấm cho tan.\n3. Ngâm rau củ vào hỗn hợp 2 tiếng."
            }
        ]
    },
    "Dưa leo": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Dưa leo trộn chua ngọt",
                "ingredients": ["2 quả dưa leo", "Giấm", "Đường", "Ớt", "Tỏi"],
                "instructions": "1. Đập dập dưa leo, cắt miếng vừa ăn.\n2. Pha giấm, đường, tỏi ớt băm.\n3. Trộn dưa leo, để ngấm 15 phút."
            },
            {
                "recipe_name": "Sinh tố dưa leo bạc hà",
                "ingredients": ["1 quả dưa leo", "Lá bạc hà", "Chanh", "Mật ong", "Đá"],
                "instructions": "1. Gọt vỏ dưa leo, cắt khúc.\n2. Xay dưa leo với bạc hà, chanh, mật ong.\n3. Thêm đá, thưởng thức lạnh."
            },
            {
                "recipe_name": "Gỏi dưa leo tôm thịt",
                "ingredients": ["2 quả dưa leo", "Tôm luộc", "Thịt ba chỉ luộc", "Đậu phộng", "Nước mắm pha"],
                "instructions": "1. Thái dưa leo sợi mỏng.\n2. Trộn với tôm, thịt thái.\n3. Rưới nước mắm pha, rắc đậu phộng rang."
            }
        ]
    },
    "Xôi": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Xôi gấc",
                "ingredients": ["500g nếp", "1 quả gấc", "Nước cốt dừa", "Đường", "Muối"],
                "instructions": "1. Ngâm nếp qua đêm, trộn với ruột gấc.\n2. Hấp xôi chín, rưới nước cốt dừa.\n3. Xới ra đĩa, rắc mè rang hoặc dừa nạo."
            },
            {
                "recipe_name": "Xôi xéo Hà Nội",
                "ingredients": ["Nếp", "Đậu xanh", "Hành phi", "Mỡ hành", "Ruốc"],
                "instructions": "1. Ngâm nếp, hấp chín. Đậu xanh hấp nghiền mịn.\n2. Xới xôi, phủ đậu xanh lên.\n3. Rưới mỡ hành, rắc hành phi, ăn kèm ruốc."
            },
            {
                "recipe_name": "Xôi mặn gà xé",
                "ingredients": ["Nếp", "Đùi gà luộc xé", "Hành phi", "Nước mắm", "Lạp xưởng"],
                "instructions": "1. Hấp nếp chín dẻo.\n2. Xé gà nhỏ, chiên lạp xưởng thái lát.\n3. Xới xôi, xếp gà, lạp xưởng, rắc hành phi."
            }
        ]
    },
    "Bò kho": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Bò kho Sài Gòn",
                "ingredients": ["500g bắp bò", "Cà rốt", "Khoai tây", "Sả", "Gừng", "Quế", "Hoa hồi", "Bột cà ri"],
                "instructions": "1. Cắt bò miếng vuông, ướp bột cà ri, sả.\n2. Xào bò lửa lớn, thêm nước hầm 2 tiếng.\n3. Cho cà rốt, khoai tây vào hầm thêm 30 phút."
            },
            {
                "recipe_name": "Bò kho nước dừa",
                "ingredients": ["500g gân bò", "Nước dừa tươi", "Cà rốt", "Sả", "Ớt hiểm", "Bột cà ri"],
                "instructions": "1. Chần gân bò, cắt miếng, ướp gia vị.\n2. Hầm gân bò với nước dừa lửa nhỏ 3 tiếng.\n3. Thêm cà rốt, nêm nếm đến khi gân mềm."
            },
            {
                "recipe_name": "Bò kho ăn kèm bún/phở",
                "ingredients": ["Bò bắp", "Cà rốt", "Sả", "Bột cà ri", "Bún/bánh phở", "Rau thơm"],
                "instructions": "1. Nấu bò kho theo cách truyền thống.\n2. Trụng bún hoặc phở ra tô.\n3. Chan nước bò kho, xếp thịt cà rốt, thêm rau thơm."
            }
        ]
    },
    "Chả giò": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Chả giò Sài Gòn",
                "ingredients": ["Bánh tráng", "Thịt heo xay", "Tôm bằm", "Mộc nhĩ", "Miến", "Cà rốt bào", "Trứng"],
                "instructions": "1. Trộn nhân thịt, tôm, mộc nhĩ, miến, cà rốt, trứng.\n2. Cuốn nhân vào bánh tráng chặt tay.\n3. Chiên ngập dầu lửa vừa đến vàng giòn."
            },
            {
                "recipe_name": "Chả giò chay",
                "ingredients": ["Bánh tráng", "Khoai môn", "Cà rốt", "Đậu xanh", "Miến", "Nấm mèo"],
                "instructions": "1. Hấp khoai môn nghiền, trộn rau củ, miến, nấm.\n2. Cuốn nhân chặt trong bánh tráng.\n3. Chiên giòn vàng, ăn kèm nước mắm chay."
            },
            {
                "recipe_name": "Chả giò hải sản",
                "ingredients": ["Bánh tráng", "Tôm", "Cua", "Thịt heo", "Mộc nhĩ", "Hành tây"],
                "instructions": "1. Bằm tôm, cua, thịt, trộn với mộc nhĩ hành.\n2. Cuốn chặt trong bánh tráng.\n3. Chiên vàng giòn, ăn kèm bún, rau sống, nước mắm."
            }
        ]
    },
    "Mì": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Mì xào bò rau cải",
                "ingredients": ["Mì trứng", "200g bò thái lát", "Cải ngọt", "Cà rốt", "Dầu hào", "Tỏi"],
                "instructions": "1. Luộc mì sơ, vớt ra trộn dầu.\n2. Xào bò lửa lớn, trút ra. Xào rau.\n3. Cho mì, bò, rau vào đảo đều, nêm dầu hào."
            },
            {
                "recipe_name": "Mì Quảng",
                "ingredients": ["Mì Quảng", "Tôm", "Thịt heo", "Trứng cút", "Đậu phộng", "Rau sống", "Bánh tráng nướng"],
                "instructions": "1. Nấu nước lèo từ xương, tôm, thêm nghệ.\n2. Luộc tôm, thái thịt, luộc trứng cút.\n3. Xếp mì, chan nước lèo ít, thêm topping và bánh tráng."
            },
            {
                "recipe_name": "Mì hoành thánh",
                "ingredients": ["Mì trứng", "Hoành thánh (thịt heo, tôm)", "Xá xíu", "Cải thìa", "Nước dùng xương"],
                "instructions": "1. Gói hoành thánh nhân tôm thịt.\n2. Nấu nước dùng xương, luộc hoành thánh.\n3. Trụng mì, chan nước dùng, xếp xá xíu, cải."
            }
        ]
    },
    "Khoai tây chiên": {
        "item_type": "dish",
        "recipes": [
            {
                "recipe_name": "Khoai tây chiên giòn kiểu Pháp",
                "ingredients": ["3 củ khoai tây", "Dầu ăn", "Muối", "Tương cà"],
                "instructions": "1. Gọt vỏ, cắt que đều. Ngâm nước lạnh 30 phút.\n2. Vớt ra lau khô, chiên lần 1 ở 130°C, vớt ra.\n3. Chiên lần 2 ở 190°C đến giòn vàng, rắc muối."
            },
            {
                "recipe_name": "Khoai tây bỏ lò phô mai",
                "ingredients": ["Khoai tây", "Phô mai mozzarella", "Bơ", "Kem chua", "Thịt xông khói"],
                "instructions": "1. Nướng khoai tây nguyên vỏ 200°C 45 phút.\n2. Xẻ đôi, dùng nĩa đánh tơi ruột, trộn bơ kem chua.\n3. Rải phô mai, thịt xông khói, nướng thêm 10 phút."
            },
            {
                "recipe_name": "Khoai tây nghiền (mashed potatoes)",
                "ingredients": ["4 củ khoai tây", "Bơ", "Sữa tươi", "Muối", "Tiêu", "Hành lá"],
                "instructions": "1. Luộc khoai chín, nghiền mịn khi còn nóng.\n2. Trộn bơ, sữa ấm từ từ đến khi mịn dẻo.\n3. Nêm muối tiêu, rắc hành lá."
            }
        ]
    },
    "Chanh": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Nước chanh muối giải khát",
                "ingredients": ["2 quả chanh muối", "Đường", "Đá viên", "Nước"],
                "instructions": "1. Dầm chanh muối với đường.\n2. Thêm nước và đá viên.\n3. Khuấy đều, thưởng thức."
            },
            {
                "recipe_name": "Gà hấp lá chanh",
                "ingredients": ["1 con gà ta", "Lá chanh", "Sả", "Muối ớt chanh"],
                "instructions": "1. Rửa gà, nhồi sả lá chanh.\n2. Hấp cách thủy 30 phút.\n3. Chặt miếng, chấm muối ớt chanh."
            },
            {
                "recipe_name": "Sốt chanh dây (passion fruit)",
                "ingredients": ["3 quả chanh dây", "Đường", "Bơ", "Trứng"],
                "instructions": "1. Đun nước chanh dây, đường, bơ lửa nhỏ.\n2. Thêm trứng đánh, khuấy liên tục.\n3. Đun đến sệt, dùng với bánh mì hoặc bánh."
            }
        ]
    },
    "Bông cải": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Bông cải xào tỏi",
                "ingredients": ["1 bông cải xanh", "Tỏi", "Dầu hào", "Nước mắm"],
                "instructions": "1. Tách bông cải thành miếng nhỏ, trụng sơ.\n2. Phi tỏi vàng, xào bông cải lửa lớn.\n3. Nêm dầu hào, nước mắm, đảo nhanh."
            },
            {
                "recipe_name": "Súp bông cải phô mai",
                "ingredients": ["Bông cải xanh", "Phô mai cheddar", "Kem tươi", "Khoai tây", "Hành tây"],
                "instructions": "1. Xào hành, khoai tây, bông cải mềm.\n2. Đổ nước dùng, đun sôi, xay nhuyễn.\n3. Thêm phô mai, kem tươi, khuấy tan."
            },
            {
                "recipe_name": "Bông cải nướng gia vị",
                "ingredients": ["Bông cải xanh", "Dầu ô liu", "Tỏi bột", "Parmesan", "Ớt bột"],
                "instructions": "1. Tách bông cải, trộn dầu ô liu, tỏi bột, muối.\n2. Nướng 200°C 20 phút đến cháy cạnh.\n3. Rắc Parmesan, ớt bột, vắt chanh."
            }
        ]
    },
    "Phô mai": {
        "item_type": "ingredient",
        "recipes": [
            {
                "recipe_name": "Bánh mì phô mai nướng (Grilled Cheese)",
                "ingredients": ["2 lát bánh mì sandwich", "Phô mai cheddar/mozzarella", "Bơ"],
                "instructions": "1. Phết bơ mặt ngoài bánh mì.\n2. Kẹp phô mai ở giữa.\n3. Nướng chảo lửa nhỏ đến vàng giòn hai mặt, phô mai chảy."
            },
            {
                "recipe_name": "Mì phô mai (Mac and Cheese)",
                "ingredients": ["Mì ống nui", "Phô mai cheddar", "Sữa tươi", "Bơ", "Bột mì"],
                "instructions": "1. Luộc mì ống al dente.\n2. Nấu sốt: tan bơ, thêm bột mì, đổ sữa khuấy đến đặc.\n3. Cho phô mai vào tan chảy, trộn mì, nướng lò 10 phút."
            },
            {
                "recipe_name": "Pizza phô mai 4 loại",
                "ingredients": ["Đế pizza", "Mozzarella", "Gorgonzola", "Parmesan", "Ricotta", "Sốt cà chua"],
                "instructions": "1. Phết sốt cà chua lên đế pizza.\n2. Rải đều 4 loại phô mai.\n3. Nướng lò 220°C 12-15 phút đến vàng rộp."
            }
        ]
    },
}

