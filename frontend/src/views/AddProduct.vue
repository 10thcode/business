<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import Compressor from 'compressorjs';
  import PageTitle from '../components/PageTitle.vue';
  import IconButton from '../components/IconButton.vue';
  import Loading from "../components/Loading.vue";
  import { useAuth0 } from '@auth0/auth0-vue'


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0();
  const loading = ref(true);
  const route = useRoute();
  const router = useRouter();
  const businessId = route.params.businessId;
  const name = ref('');
  const short_description = ref('');
  const long_description = ref('');
  const currency = ref('');
  const amount = ref(undefined);
  const availability = ref(false);
  const image = ref(null);


  function handleMainImage (event) {
    const mainImage = event.target.files[0];

    if (mainImage) {
      new Compressor(mainImage, {
        quality: 0.4,
        success: (result) => {
          image.value = new File([result], result.name);
        },
        error: (err) => {
          throw new Error("Image Compression error");
        }
      });
    }
  }


  async function addProduct () {
    loading.value = true;
    if (await isAuthenticated.value) {
      const formData = new FormData();

      formData.append('business', businessId);
      formData.append('name', name.value);
      formData.append('short_description', short_description.value);
      formData.append('long_description', long_description.value);
      formData.append('currency', currency.value);
      formData.append('amount', amount.value);
      formData.append('availability', availability.value);
      if (image.value) {
        formData.append('image', image.value);
      }

      const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/products/?user=${user.value.sub}`, {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error("Server error");
      }

      const data = await response.json();

      router.push(`/businesses/${businessId}/products/${data.id}`)
    }

    loading.value = false;
  }


  onMounted(async () => {
    if (!await isAuthenticated.value) {
      router.push('/account/login');
    }
    loading.value = false;
  });
</script>

<template>
  <Loading v-if="loading"/>
  <PageTitle>Add product</PageTitle>
  <section class="form-container">
    <form @submit.prevent="addProduct">
      <div class="field">
        <label for="name">Name *</label>
        <input
          required
          id="name"
          type="text"
          maxlength="60"
          placeholder="eg. Smartphone X"
          v-model="name"
        >
      </div>
      <div class="field">
        <label for="short_description">Short description *</label>
        <textarea
          required
          id="short_description"
          maxlength="120"
          placeholder="eg. Compact and powerful smartphone with advanced features ..."
          v-model="short_description"
        ></textarea>
      </div>
      <div class="field">
        <label for="long_description">Long description</label>
        <textarea
          id="long_description"
          maxlength="360"
          placeholder="eg. The Smartphone X combines sleek design with cutting-edge technology ..."
          v-model="long_description"
        ></textarea>
      </div>
      <div class="field">
        <label for="currency">Currency *</label>
        <select id="day" v-model="currency" required>
          <option value="" selected disabled>Select currency</option>
          <option value="AED">AED - United Arab Emirates Dirham</option>
          <option value="AFN">AFN - Afghan Afghani</option>
          <option value="ALL">ALL - Albanian Lek</option>
          <option value="AMD">AMD - Armenian Dram</option>
          <option value="ANG">ANG - Netherlands Antillean Guilder</option>
          <option value="AOA">AOA - Angolan Kwanza</option>
          <option value="ARS">ARS - Argentine Peso</option>
          <option value="AUD">AUD - Australian Dollar</option>
          <option value="AWG">AWG - Aruban Florin</option>
          <option value="AZN">AZN - Azerbaijani Manat</option>
          <option value="BAM">BAM - Bosnia-Herzegovina Convertible Mark</option>
          <option value="BBD">BBD - Barbadian Dollar</option>
          <option value="BDT">BDT - Bangladeshi Taka</option>
          <option value="BGN">BGN - Bulgarian Lev</option>
          <option value="BHD">BHD - Bahraini Dinar</option>
          <option value="BIF">BIF - Burundian Franc</option>
          <option value="BMD">BMD - Bermudian Dollar</option>
          <option value="BND">BND - Brunei Dollar</option>
          <option value="BOB">BOB - Bolivian Boliviano</option>
          <option value="BRL">BRL - Brazilian Real</option>
          <option value="BSD">BSD - Bahamian Dollar</option>
          <option value="BTN">BTN - Bhutanese Ngultrum</option>
          <option value="BWP">BWP - Botswanan Pula</option>
          <option value="BYN">BYN - Belarusian Ruble</option>
          <option value="BZD">BZD - Belize Dollar</option>
          <option value="CAD">CAD - Canadian Dollar</option>
          <option value="CDF">CDF - Congolese Franc</option>
          <option value="CHF">CHF - Swiss Franc</option>
          <option value="CLP">CLP - Chilean Peso</option>
          <option value="CNY">CNY - Chinese Yuan</option>
          <option value="COP">COP - Colombian Peso</option>
          <option value="CRC">CRC - Costa Rican Colón</option>
          <option value="CUP">CUP - Cuban Peso</option>
          <option value="CVE">CVE - Cape Verdean Escudo</option>
          <option value="CZK">CZK - Czech Republic Koruna</option>
          <option value="DJF">DJF - Djiboutian Franc</option>
          <option value="DKK">DKK - Danish Krone</option>
          <option value="DOP">DOP - Dominican Peso</option>
          <option value="DZD">DZD - Algerian Dinar</option>
          <option value="EGP">EGP - Egyptian Pound</option>
          <option value="ERN">ERN - Eritrean Nakfa</option>
          <option value="ETB">ETB - Ethiopian Birr</option>
          <option value="EUR">EUR - Euro</option>
          <option value="FJD">FJD - Fijian Dollar</option>
          <option value="FKP">FKP - Falkland Islands Pound</option>
          <option value="FOK">FOK - Faroese Króna</option>
          <option value="GBP">GBP - British Pound Sterling</option>
          <option value="GEL">GEL - Georgian Lari</option>
          <option value="GGP">GGP - Guernsey Pound</option>
          <option value="GHS">GHS - Ghanaian Cedi</option>
          <option value="GIP">GIP - Gibraltar Pound</option>
          <option value="GMD">GMD - Gambian Dalasi</option>
          <option value="GNF">GNF - Guinean Franc</option>
          <option value="GTQ">GTQ - Guatemalan Quetzal</option>
          <option value="GYD">GYD - Guyanaese Dollar</option>
          <option value="HKD">HKD - Hong Kong Dollar</option>
          <option value="HNL">HNL - Honduran Lempira</option>
          <option value="HRK">HRK - Croatian Kuna</option>
          <option value="HTG">HTG - Haitian Gourde</option>
          <option value="HUF">HUF - Hungarian Forint</option>
          <option value="IDR">IDR - Indonesian Rupiah</option>
          <option value="ILS">ILS - Israeli New Sheqel</option>
          <option value="IMP">IMP - Isle of Man Pound</option>
          <option value="INR">INR - Indian Rupee</option>
          <option value="IQD">IQD - Iraqi Dinar</option>
          <option value="IRR">IRR - Iranian Rial</option>
          <option value="ISK">ISK - Icelandic Króna</option>
          <option value="JEP">JEP - Jersey Pound</option>
          <option value="JMD">JMD - Jamaican Dollar</option>
          <option value="JOD">JOD - Jordanian Dinar</option>
          <option value="JPY">JPY - Japanese Yen</option>
          <option value="KES">KES - Kenyan Shilling</option>
          <option value="KGS">KGS - Kyrgystani Som</option>
          <option value="KHR">KHR - Cambodian Riel</option>
          <option value="KID">KID - Kiribati Dollar</option>
          <option value="KMF">KMF - Comorian Franc</option>
          <option value="KRW">KRW - South Korean Won</option>
          <option value="KWD">KWD - Kuwaiti Dinar</option>
          <option value="KYD">KYD - Cayman Islands Dollar</option>
          <option value="KZT">KZT - Kazakhstani Tenge</option>
          <option value="LAK">LAK - Laotian Kip</option>
          <option value="LBP">LBP - Lebanese Pound</option>
          <option value="LKR">LKR - Sri Lankan Rupee</option>
          <option value="LRD">LRD - Liberian Dollar</option>
          <option value="LSL">LSL - Lesotho Loti</option>
          <option value="LYD">LYD - Libyan Dinar</option>
          <option value="MAD">MAD - Moroccan Dirham</option>
          <option value="MDL">MDL - Moldovan Leu</option>
          <option value="MGA">MGA - Malagasy Ariary</option>
          <option value="MKD">MKD - Macedonian Denar</option>
          <option value="MMK">MMK - Myanma Kyat</option>
          <option value="MNT">MNT - Mongolian Tugrik</option>
          <option value="MOP">MOP - Macanese Pataca</option>
          <option value="MRU">MRU - Mauritanian Ouguiya</option>
          <option value="MUR">MUR - Mauritian Rupee</option>
          <option value="MVR">MVR - Maldivian Rufiyaa</option>
          <option value="MWK">MWK - Malawian Kwacha</option>
          <option value="MXN">MXN - Mexican Peso</option>
          <option value="MYR">MYR - Malaysian Ringgit</option>
          <option value="MZN">MZN - Mozambican Metical</option>
          <option value="NAD">NAD - Namibian Dollar</option>
          <option value="NGN">NGN - Nigerian Naira</option>
          <option value="NIO">NIO - Nicaraguan Córdoba</option>
          <option value="NOK">NOK - Norwegian Krone</option>
          <option value="NPR">NPR - Nepalese Rupee</option>
          <option value="NZD">NZD - New Zealand Dollar</option>
          <option value="OMR">OMR - Omani Rial</option>
          <option value="PAB">PAB - Panamanian Balboa</option>
          <option value="PEN">PEN - Peruvian Nuevo Sol</option>
          <option value="PGK">PGK - Papua New Guinean Kina</option>
          <option value="PHP">PHP - Philippine Peso</option>
          <option value="PKR">PKR - Pakistani Rupee</option>
          <option value="PLN">PLN - Polish Zloty</option>
          <option value="PYG">PYG - Paraguayan Guarani</option>
          <option value="QAR">QAR - Qatari Rial</option>
          <option value="RON">RON - Romanian Leu</option>
          <option value="RSD">RSD - Serbian Dinar</option>
          <option value="RUB">RUB - Russian Ruble</option>
          <option value="RWF">RWF - Rwandan Franc</option>
          <option value="SAR">SAR - Saudi Riyal</option>
          <option value="SBD">SBD - Solomon Islands Dollar</option>
          <option value="SCR">SCR - Seychellois Rupee</option>
          <option value="SDG">SDG - Sudanese Pound</option>
          <option value="SEK">SEK - Swedish Krona</option>
          <option value="SGD">SGD - Singapore Dollar</option>
          <option value="SHP">SHP - Saint Helena Pound</option>
          <option value="SLL">SLL - Sierra Leonean Leone</option>
          <option value="SOS">SOS - Somali Shilling</option>
          <option value="SPL">SPL - Seborgan Luigino</option>
          <option value="SRD">SRD - Surinamese Dollar</option>
          <option value="STN">STN - São Tomé & Príncipe Dobra</option>
          <option value="SYP">SYP - Syrian Pound</option>
          <option value="SZL">SZL - Swazi Lilangeni</option>
          <option value="THB">THB - Thai Baht</option>
          <option value="TJS">TJS - Tajikistani Somoni</option>
          <option value="TMT">TMT - Turkmenistani Manat</option>
          <option value="TND">TND - Tunisian Dinar</option>
          <option value="TOP">TOP - Tongan Pa'anga</option>
          <option value="TRY">TRY - Turkish Lira</option>
          <option value="TTD">TTD - Trinidad & Tobago Dollar</option>
          <option value="TVD">TVD - Tuvaluan Dollar</option>
          <option value="TWD">TWD - New Taiwan Dollar</option>
          <option value="TZS">TZS - Tanzanian Shilling</option>
          <option value="UAH">UAH - Ukrainian Hryvnia</option>
          <option value="UGX">UGX - Ugandan Shilling</option>
          <option value="USD">USD - United States Dollar</option>
          <option value="UYU">UYU - Uruguayan Peso</option>
          <option value="UZS">UZS - Uzbekistan Som</option>
          <option value="VES">VES - Venezuelan Bolívar</option>
          <option value="VND">VND - Vietnamese Dong</option>
          <option value="VUV">VUV - Vanuatu Vatu</option>
          <option value="WST">WST - Samoan Tala</option>
          <option value="XAF">XAF - Central African CFA Franc</option>
          <option value="XCD">XCD - East Caribbean Dollar</option>
          <option value="XDR">XDR - Special Drawing Rights</option>
          <option value="XOF">XOF - West African CFA Franc</option>
          <option value="XPF">XPF - CFP Franc</option>
          <option value="YER">YER - Yemeni Rial</option>
          <option value="ZAR">ZAR - South African Rand</option>
          <option value="ZMW">ZMW - Zambian Kwacha</option>
          <option value="ZWL">ZWL - Zimbabwean Dollar</option>
        </select>
      </div>
      <div class="field">
        <label for="amount">Amount *</label>
        <input
          required
          id="amount"
          type="number"
          step="0.01"
          placeholder="eg. 599.99"
          v-model="amount"
        >
      </div>
      <div class="field">
        <label for="availability">In stock</label>
        <input
          id="availability"
          type="checkbox"
          v-model="availability"
        >
      </div>
      <div class="field">
        <label for="main_image">Main image</label>
        <input
          type="file"
          id="main_image"
          accept="image/*"
          @change="handleMainImage"
        >
      </div>
      <div class="form-buttons action-buttons">
        <IconButton
          @click="$router.push(`/businesses/${businessId}`)"
          type="button" color="accent" icon="close"/>
        <IconButton type="submit" color="solid-accent" icon="add">Add &nbsp</IconButton>
      </div>
    </form>
  </section>
</template>
