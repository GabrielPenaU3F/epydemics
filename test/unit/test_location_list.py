import unittest

from src.data_manipulation.data_manager import DataManager


class LocationListTests(unittest.TestCase):

    def test_owid_location_list_is_correct(self):
        DataManager.load_dataset('owid', 'owid_dataset.csv')
        owid_locations = ['Afghanistan', 'Africa', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla',
         'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Asia', 'Australia', 'Austria',
         'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
         'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire Sint Eustatius and Saba',
         'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
         'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic',
         'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica',
         "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czechia',
         'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica',
         'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
         'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Europe', 'European Union', 'Faeroe Islands', 'Falkland Islands',
         'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece',
         'Greenland', 'Grenada', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras',
         'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'International',
         'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan',
         'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia',
         'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
         'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
         'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
         'Micronesia (country)', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat',
         'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia',
         'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North America', 'North Macedonia', 'Northern Cyprus',
         'Norway', 'Oceania', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay',
         'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia',
         'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia',
         'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
         'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
         'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands',
         'Somalia', 'South Africa', 'South America', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka',
         'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan',
         'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkmenistan', 'Tuvalu',
         'Turkey', 'Turks and Caicos Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom',
         'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican', 'Venezuela', 'Wallis and Futuna',
         'Vietnam', 'World', 'Yemen', 'Zambia', 'Zimbabwe']
        actual_locations = list(DataManager.get_location_list())
        self.assertCountEqual(owid_locations, actual_locations)

    def test_mapache_arg_location_list_is_correct(self):
        DataManager.load_dataset('mapache_arg', 'mapache_arg_dataset.csv')
        mapache_locations = ['Buenos Aires', 'Indeterminado', 'CABA', 'Córdoba', 'Mendoza', 'Santa Cruz', 'Tierra del Fuego', 'Formosa',
                             'San Juan', 'Corrientes', 'Santa Fe', 'Salta', 'Misiones', 'Entre Ríos', 'La Rioja',
                             'Río Negro', 'Chaco', 'San Luis', 'Tucumán', 'Neuquén', 'La Pampa', 'Catamarca',
                             'Chubut', 'Jujuy', 'Santiago del Estero']
        actual_locations = list(DataManager.get_location_list())
        self.assertCountEqual(mapache_locations, actual_locations)


if __name__ == '__main__':
    unittest.main()
