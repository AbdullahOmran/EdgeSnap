from TestAPIClient import TestAPIClient


client_test = TestAPIClient()

client_test.test_get_grayscale()
client_test.test_add_salt_and_pepper_noise(saltiness=0,pepperiness=0.2)
client_test.test_gaussian_blur()