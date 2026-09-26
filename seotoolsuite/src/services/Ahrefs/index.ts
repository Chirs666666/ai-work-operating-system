import axios from "axios";

/**
 * Ahrefs service.
 */
class Ahrefs {
  /**
   * Ahrefs API URL.
   */
  private API_BASE_URL: string;

  /**
   * Ahrefs API key.
   */
  private API_KEY: string;

  /**
   * Constructor.
   */
  constructor() {
    if (!process.env.AHREFS_API_KEY)
      throw new Error("AHREFS_API_KEY is not defined in the environment.");

    this.API_BASE_URL = "https://api.ahrefs.com/v3";
    this.API_KEY = process.env.AHREFS_API_KEY;
  }

  /**
   * Get Ahrefs domain rating (free).
   */
  async getDomainRatingFree(target: string): Promise<number> {
    try {
      const apiResponse = await axios.get(
        `${this.API_BASE_URL}/public/domain-rating-free`,
        {
          headers: {
            Authorization: `Bearer ${this.API_KEY}`,
          },
          params: {
            target,
            output: "json",
          },
        },
      );

      return apiResponse?.data?.domain_rating?.domain_rating;
    } catch (error) {
      throw error;
    }
  }
}

export default Ahrefs;
