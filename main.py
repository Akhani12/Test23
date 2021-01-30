import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import cv2
import io
import base64

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    p_bs_img = request.args['product_image']
    imgdata = base64.b64decode(str(p_bs_img))
    image = Image.open(io.BytesIO(imgdata))
    cv_img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

    def category_predict(label_no):
        if label_no == 0:
            return "ilha do campche"
        elif label_no == 1:
            return "CSSD_ROVINJ"
        elif label_no == 2:
            return "Kruger national park"
        elif label_no == 3:
            return "amalfi coast"
        elif label_no == 4:
            return "angkor wat, cambodia"
        elif label_no == 5:
            return "bali swing ubud bali"
        elif label_no == 6:
            return "cambuagahay falls phillipines"
        elif label_no == 7:
            return "cannoying empire falls blue mountains australia"
        elif label_no == 8:
            return "cappadocia"
        elif label_no == 9:
            return "cherry blossom japan"
        elif label_no == 10:
            return "cijevna motenegro"
        elif label_no == 11:
            return "geiranger fjord norway"
        elif label_no == 12:
            return "grand canyon"
        elif label_no == 13:
            return "green village bali"
        elif label_no == 14:
            return "huacachina ica peru"
        elif label_no == 15:
            return "java iceland"
        elif label_no == 16:
            return "infinity pool singapore"
        elif label_no == 17:
            return "jesus statue rio de janeiro"
        elif label_no == 18:
            return "Kanhura maldives"
        elif label_no == 19:
            return "kon ha lagoon thailand"
        elif label_no == 20:
            return "kravice montenegro"
        elif label_no == 21:
            return "lake of bled slovenia"
        elif label_no == 22:
            return "lake tahoe nevada"
        elif label_no == 23:
            return "lauter brunnen"
        elif label_no == 24:
            return "machu pichu"
        elif label_no == 25:
            return "matadeiro beach"
        elif label_no == 26:
            return "mont_saint_michel_normandy_france"
        elif label_no == 27:
            return "multnomah_falls,oregon,united_states"
        elif label_no == 28:
            return "mykonos greece"
        elif label_no == 29:
            return "Nathula pass sikkim india"
        elif label_no == 30:
            return "nusa penida bali"
        elif label_no == 31:
            return "pangong lake ladhakh"
        elif label_no == 32:
            return "paro bhutan"
        elif label_no == 33:
            return "plansee tirol austria"
        elif label_no == 34:
            return "ribeirao da ilha brasil"
        elif label_no == 35:
            return "stairway to heaven hawaii"
        elif label_no == 36:
            return "stryn norway"
        elif label_no == 37:
            return "the edge bali"
        elif label_no == 38:
            return "Tracy arm fjord alaska"
        elif label_no == 39:
            return "tromso norway"
        elif label_no == 40:
            return "tosmgo lake sikkim"
        elif label_no == 41:
            return "Tulip garden netherland"
        elif label_no == 42:
            return "Underwater resort maldives"
        elif label_no == 43:
            return "voss norway"

    def label_predict(label_no):
        if label_no == "1_iladecampche":
            return 0
        elif label_no == "CSSD_ROVINJ":
            return 1
        elif label_no == "Kruger_national_park":
            return 2
        elif label_no == "amalfi_coast":
            return 3
        elif label_no == "angkor_wat_combodia":
            return 4
        elif label_no == "bali_swing_ubud_bali":
            return 5
        elif label_no == "cambugahay_falls_siquijor_philippines":
            return 6
        elif label_no == "canonying_empire_falls_blue_mountains_australia":
            return 7
        elif label_no == "cappadocia":
            return 8
        elif label_no == "cherry_blossom_japan":
            return 9
        elif label_no == "cijevna_montenegro":
            return 10
        elif label_no == "geiranger_fjord_norway":
            return 11
        elif label_no == "grand_canyon":
            return 12
        elif label_no == "green_village_bali":
            return 13
        elif label_no == "huacachina_ica_peru":
            return 14
        elif label_no == "ijencraterjavaisland":
            return 15
        elif label_no == "infinity_pool_singapore":
            return 16
        elif label_no == "jesus_statue,_rio_de_janeiro":
            return 17
        elif label_no == "kanuhura_maldives":
            return 18
        elif label_no == "koh_ha_lagoon_,_thailand":
            return 19
        elif label_no == "kravice_montenegro":
            return 20
        elif label_no == "lake_of_bled,_slovenia":
            return 21
        elif label_no == "lake_tahoe_nevada":
            return 22
        elif label_no == "lauterbrunnen":
            return 23
        elif label_no == "machu_pichu":
            return 24
        elif label_no == "matadeiro_beach":
            return 25
        elif label_no == "mont_saint_michel_normandy_france":
            return 26
        elif label_no == "multnomah_falls,oregon,united_states":
            return 27
        elif label_no == "mykonos_greece":
            return 28
        elif label_no == "nathula_pass_sikkim_india":
            return 29
        elif label_no == "nusa_penida_bali":
            return 30
        elif label_no == "pangong_lake_ladhakh":
            return 31
        elif label_no == "paro_bhutan":
            return 32
        elif label_no == "plansee_tirol_austria":
            return 33
        elif label_no == "ribeirao_da_ilha_brasil":
            return 34
        elif label_no == "stariway_to_heaven_hike,oahu,hawaii":
            return 35
        elif label_no == "stryn,norway":
            return 36
        elif label_no == "the_edge_bali":
            return 37
        elif label_no == "tracy_arm_fjord,alaska":
            return 38
        elif label_no == "tromso,_norway":
            return 39
        elif label_no == "tsomgo_lake_sikkim_india":
            return 40
        elif label_no == "tulip_garden_netherlands":
            return 41
        elif label_no == "underwater_resorts_maldives":
            return 42
        elif label_no == "voss_norway":
            return 43

    def model_predict(img_path):
        img = cv2.resize(img_path, (224, 224))

        # Preprocessing the image
        img = img.reshape(1, 224, 224, 3)
        imd = np.array(img)

        model = load_model('./Location_identification_model.h5')
        preds = model.predict(imd)

        label_no = np.argmax(preds)
        out = category_predict(label_no)
        return out

    # Input image path
    location_name = model_predict(cv_img)
    print('Location name:', location_name)

    # Create Json
    output_json = {'Location_name': location_name}

    return output_json


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
