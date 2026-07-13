import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  // The entry point of the app, Flutter starts here.
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    // MaterialApp is the root of the app and sets up the theme.
    return MaterialApp(
      title: 'Weather App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const WeatherPage(),
    );
  }
}

class WeatherPage extends StatefulWidget {
  const WeatherPage({super.key});

  @override
  State<WeatherPage> createState() => _WeatherPageState();
}

class _WeatherPageState extends State<WeatherPage> {
  final TextEditingController _cityController = TextEditingController();
  bool _isLoading = false;
  String _weatherDescription = '';
  String _temperature = '';
  String _errorMessage = '';

  // Replace this value with your own OpenWeatherMap API key.
  static const String _apiKey = 'YOUR_API_KEY_HERE';

  Future<void> _fetchWeather(String city) async {
    setState(() {
      _isLoading = true;
      _errorMessage = '';
    });

    try {
      // Build the URL to query the OpenWeatherMap API.
      final uri = Uri.https(
        'api.openweathermap.org',
        '/data/2.5/weather',
        {
          'q': city,
          'appid': _apiKey,
          'units': 'metric',
        },
      );

      final response = await http.get(uri);

      if (response.statusCode == 200) {
        // Decode the JSON response and update the UI.
        final data = jsonDecode(response.body) as Map<String, dynamic>;
        final weather = data['weather'] as List<dynamic>;
        final main = data['main'] as Map<String, dynamic>;

        setState(() {
          _weatherDescription = weather.isNotEmpty
              ? weather[0]['description'] as String
              : 'No description';
          _temperature = '${main['temp'].toString()} °C';
        });
      } else {
        setState(() {
          _errorMessage = 'Could not load weather for "$city".';
        });
      }
    } catch (error) {
      setState(() {
        _errorMessage = 'An error occurred: $error';
      });
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    // The main screen for the weather app.
    return Scaffold(
      appBar: AppBar(
        title: const Text('Weather App'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'Enter a city name to fetch the current weather.',
              style: TextStyle(fontSize: 16),
            ),
            const SizedBox(height: 16),
            TextField(
              controller: _cityController,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'City',
                hintText: 'e.g. London',
              ),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: _isLoading
                  ? null
                  : () {
                      final city = _cityController.text.trim();
                      if (city.isNotEmpty) {
                        _fetchWeather(city);
                      }
                    },
              child: _isLoading
                  ? const SizedBox(
                      height: 16,
                      width: 16,
                      child: CircularProgressIndicator(
                        strokeWidth: 2,
                        color: Colors.white,
                      ),
                    )
                  : const Text('Get Weather'),
            ),
            const SizedBox(height: 24),
            if (_errorMessage.isNotEmpty) ...[
              Text(
                _errorMessage,
                style: const TextStyle(color: Colors.red),
              ),
              const SizedBox(height: 16),
            ],
            if (_weatherDescription.isNotEmpty) ...[
              Card(
                elevation: 2,
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Description: $_weatherDescription',
                        style: const TextStyle(fontSize: 18),
                      ),
                      const SizedBox(height: 8),
                      Text(
                        'Temperature: $_temperature',
                        style: const TextStyle(fontSize: 18),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }
}
