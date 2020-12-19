(ns day_xx.solution
  (:require [clojure.string :as str]
            [main :as main :refer [defoverload]]))

(def day "xx")

(defn get-lines
  "Read in and parse inputs as seq of vectors."
  [file]
  (->> file
       slurp
       str/split-lines
       (map identity)))

(defn part1
  [_]
  nil)

(defn part2
  [_]
  nil)

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)
