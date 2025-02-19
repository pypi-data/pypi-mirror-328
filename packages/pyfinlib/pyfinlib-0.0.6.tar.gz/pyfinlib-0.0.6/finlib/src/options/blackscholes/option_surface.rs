use core::ops::Range;
use std::sync::{Arc, Mutex};
use crate::options::blackscholes::{CallOption, Option, OptionVariables, PutOption};

pub struct OptionSurface {
    underlying_price: Range<isize>,
    underlying_price_bounds: (f64, f64),
    strike_price: Range<isize>,
    strike_price_bounds: (f64, f64),
    volatility: Range<isize>,
    volatility_bounds: (f64, f64),
    risk_free_interest_rate: Range<isize>,
    risk_free_interest_rate_bounds: (f64, f64),
    dividend: Range<isize>,
    dividend_bounds: (f64, f64),
    time_to_expiration: Range<isize>,
    time_to_expiration_bounds: (f64, f64)
}

impl OptionSurface {
    pub fn from(underlying_price: Range<isize>,
                underlying_price_bounds: (f64, f64),
                strike_price: Range<isize>,
                strike_price_bounds: (f64, f64),
                volatility: Range<isize>,
                volatility_bounds: (f64, f64),
                risk_free_interest_rate: Range<isize>,
                risk_free_interest_rate_bounds: (f64, f64),
                dividend: Range<isize>,
                dividend_bounds: (f64, f64),
                time_to_expiration: Range<isize>,
                time_to_expiration_bounds: (f64, f64)) -> Self {
        Self {
            underlying_price,
            underlying_price_bounds,
            strike_price,
            strike_price_bounds,
            volatility,
            volatility_bounds,
            risk_free_interest_rate,
            risk_free_interest_rate_bounds,
            dividend,
            dividend_bounds,
            time_to_expiration,
            time_to_expiration_bounds,
        }
    }

    pub fn walk(self) -> Vec<OptionVariables> {

        let mut vec: Vec<OptionVariables> = Vec::with_capacity(
            self.underlying_price.len()
            * self.strike_price.len()
            * self.volatility.len()
            * self.risk_free_interest_rate.len()
            * self.dividend.len()
            * self.time_to_expiration.len()
        );
        for p in self.underlying_price {
            for s in self.strike_price.clone() {
                for v in self.volatility.clone() {
                    for i in self.risk_free_interest_rate.clone() {
                        for d in self.dividend.clone() {
                            for t in self.time_to_expiration.clone() {
                                let v = OptionVariables::from(
                                    self.underlying_price_bounds.0 + (self.underlying_price_bounds.1 - self.underlying_price_bounds.0) * p as f64,
                                    self.strike_price_bounds.0 + (self.strike_price_bounds.1 - self.strike_price_bounds.0) * s as f64,
                                    self.volatility_bounds.0 + (self.volatility_bounds.1 - self.volatility_bounds.0) * v as f64,
                                    self.risk_free_interest_rate_bounds.0 + (self.risk_free_interest_rate_bounds.1 - self.risk_free_interest_rate_bounds.0) * i as f64,
                                    self.dividend_bounds.0 + (self.dividend_bounds.1 - self.dividend_bounds.0) * d as f64,
                                    self.time_to_expiration_bounds.0 + (self.time_to_expiration_bounds.1 - self.time_to_expiration_bounds.0) * t as f64
                                );
                                vec.push(v);
                            }
                        }
                    }
                }
            }
        }

        vec
    }
}

#[cfg(test)]
mod tests {
    use crate::options::blackscholes::{generate_options, CallOption, Option, PutOption};
    use super::*;

    #[test]
    fn walk_test() {
        let w = OptionSurface::from(
            (0 .. 50),
            (100., 200.),
            (0 .. 50),
            (100., 200.),
            (0 .. 5),
            (0.25, 0.50),
            (0 .. 10),
            (0.05, 0.08),
            (0 .. 1),
            (0.01, 0.02),
            (0 .. 10),
            (30./365.25, 30./365.25),
        );

        let a = w.walk();

        let options = generate_options(&a);

        let a1 = a.first();
    }
}